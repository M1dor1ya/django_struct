# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 10:31
# @Author  : Zcs
# @File    : urls.py.py
from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
