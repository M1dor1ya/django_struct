# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 10:31
# @Author  : Zcs
# @File    : urls.py.py
"""
url方法为Django 1.X推荐使用的，Django2.0请使用path和re_path方法
"""
#  from django.conf.urls import url
from django.conf.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path(r'network/dev/', views.DevInfo.as_view()),
    # path(r'snippets/(?P<pk>[0-9]+)/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
