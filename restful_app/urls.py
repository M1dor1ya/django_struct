# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 10:31
# @Author  : Zcs
# @File    : urls.py.py
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^network/dev/$', views.DevInfo.as_view()),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
