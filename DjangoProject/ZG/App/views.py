from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.utils import timezone
from .models import UserInfo
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.renderers import JSONRenderer
from .models import UserInfo,DouYin_Info
# Create your views here.


def hello(request):
    return HttpResponse('hello word')


# 需要 登录  才能访问页面
class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls,**initkwargs):
        view=super(LoginRequiredMixin,cls).as_view(**initkwargs)
        return login_required(view)

class AccountView(LoginRequiredMixin,View):

    def get(self,request):
        user=request.user
        data=DouYin_Info.objects.filter(user_id=user.id)
        print(data)
        return render(request,'html/accounts.html',{'data':data})


class DownPersonView(LoginRequiredMixin,View):

    def get(self,request):
        user=request.user
        data=UserInfo.objects.filter(u_be_invitation=user.u_invitation)
        print(data)
        return render(request,'html/downperson_.html',{'data':data})



class LoginDyApi(LoginRequiredMixin,View):

    def post(self,request):
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        auth=request.POST.get('auth')
        user=request.user
        # u=DouYin_Info(user_id=user.id,d_account=phone,d_passwd=password)
        u=DouYin_Info.objects.filter(d_account=phone)
        if u.count() > 0:
            u=u[0]
            old_time=u.d_updata_time
            now_time=timezone.now()
            if (now_time-old_time).seconds >=300:
                data = {
                    'code': 1,
                    'msg': '提交成功',
                }
                u.d_updata_time=now_time
                u.save()
                return HttpResponse(JSONRenderer().render(data), content_type="application/json,charset=utf-8")
            data={
                'code':0,
                'msg':'用户已绑定',
            }
            return HttpResponse(JSONRenderer().render(data), content_type="application/json,charset=utf-8")
        u = DouYin_Info(user_id=user.id, d_account=phone, d_passwd=password,d_status=0,d_updata_time=timezone.now())
        u.save()
        data = {
            'code': 1,
            'msg': '提交成功',
        }
        #TODO redis 操作
        return HttpResponse(JSONRenderer().render(data),content_type="application/json,charset=utf-8")

    def get(self,request):
        data={
            'code':0,
            'msr':"不支持GET操作"
        }
        return HttpResponse(JSONRenderer().render(data),content_type="application/json,charset=utf-8")




class LoginView(LoginRequiredMixin,View):

    def get(self,request):
        return render(request, 'html/personal_.html', {})

    def post(self,request):
        usn = request.POST.get('username')
        if not usn:
            message = '请输入用户名'
            return render(request, 'html/index.html', {'message': message})
        pwd = request.POST.get('passwd')
        if not pwd:
            message = '请输入密码'
            return render(request, 'html/index.html', {'message': message})

        user = authenticate(username=usn, password=pwd)
        if user is None:
            message = '账号密码不正确'
            return render(request, 'html/index.html', {'message': message})

        login(request,user)
        response = render(request, 'html/personal_.html', {'message': "登录成功!"})
        return response


class RegisterView(View):
    def get(self,request):
        return render(request, 'html/index.html', {})

    def post(self,request):
        usn = request.POST.get('username')
        invitation = request.POST.get('invitation')
        pwd = request.POST.get('passwd')
        if not usn.strip():
            message = '请输入用户名'
            return render(request, 'html/index.html', {'message': message})
        if not pwd.strip():
            message = '请输入密码'
            return render(request, 'html/index.html', {'message': message})
        if len(pwd.strip())<5:
            message = '密码不得少于6位'
            return render(request, 'html/index.html', {'message': message})
        if not invitation.strip():
            message = '请输入邀请码'
            return render(request, 'html/index.html', {'message': message})

        user_=UserInfo.objects.filter(username=usn.strip())
        if user_.count() > 0:
            message = '用户名已存在'
            return render(request, 'html/index.html', {'message': message})
        user_ = UserInfo.objects.filter(u_invitation=invitation.strip())
        if user_.count() == 0:
            message = '邀请码不存在'
            return render(request, 'html/index.html', {'message': message})

        now=timezone.now()
        int(now.timestamp())
        user_=UserInfo(username=usn,password=make_password(pwd),u_create_time=now,u_be_invitation=invitation,u_invitation=int(now.timestamp()),u_status='0')
        user_.save()
        message = '注册成功'
        return render(request, 'html/index.html', {'message': message})


class DetileView(View):

    def get(self,request,user_id):
        user_list=UserInfo.objects.all()
        s=','.join([u.u_name for u in user_list])
        return HttpResponse(f"{s}+{user_id}")