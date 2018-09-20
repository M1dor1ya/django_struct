# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 10:31
# @Author  : Zcs
# @File    : urls.py.py
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

urlpatterns = [
    url(r'^login/', obtain_jwt_token),
    url(r'^token-verify/', verify_jwt_token),
]

#  此处的URL为绝对URL，请求必须和所规定URL保持一致
#  例如 login/ 如果不带反斜杠会报错


