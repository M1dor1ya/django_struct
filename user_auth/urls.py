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


