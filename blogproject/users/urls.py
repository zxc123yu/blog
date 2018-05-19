# coding=utf-8
# -*- coding:utf-8 -*-
# author:天际
# datetime:2018/5/19 16:43
# software: PyCharm
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
app_name = 'users'
urlpatterns = [
	url(r'^login/$',login,{'template_name': 'users/login.html'},name='login'),
]