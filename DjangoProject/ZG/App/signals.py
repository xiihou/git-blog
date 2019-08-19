from django.core.signals import request_finished,request_started

from django.dispatch import receiver


# def my_callback(sender,**kwargs):
#     print('111')
#
# request_finished.connect(my_callback)
#
# @receiver(request_started)
# def my_handler(sender,**kwargs):
#     print('222')

# 自定义信号
# from django.dispatch import Signal
# #
# # # providing_args 需要传递的参数
# # change_password_signal = Signal(providing_args=[])
# # # 触发信号
# # change_password_signal.send(sender='')