"""ZG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from .views import *

def index(request):
    return render(request,'html/index.html',{})


urlpatterns = [
    re_path('^$',index,name='index'),
    re_path('^api/logindy/',LoginDyApi.as_view(),name='logindy'),
    re_path('^login/',LoginView.as_view(),name='login'),
    re_path('^regiter/',RegisterView.as_view(),name='regiter'),
    re_path('^detile/(?P<user_id>[0-9]+)',DetileView.as_view(),name='detile'),
    re_path('^hello/',hello,name='hello'),
    re_path('^accounts/',AccountView.as_view(),name='accounts'),
    re_path('^downperson/',DownPersonView.as_view(),name='downperson'),
]
