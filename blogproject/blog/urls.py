# coding=utf-8
# -*- coding:utf-8 -*-
# author:天际
# datetime:2018/5/16 14:03
# software: PyCharm
from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
	url(r'^$',views.IndexView.as_view(),name='index'),
	url(r'^article/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.ArchivesView.as_view(),name='archives'),
	url(r'^category/(?P<pk>[0-9]+)/$',views.CategoryView.as_view(),name='category'),
	url(r'^new_category/$',views.new_category,name='new_category'),
	url(r'^new_tag/$',views.new_tag,name='new_tag'),
	url(r'^new_article/$',views.new_article,name='new_article'),
	#url(r'^edit_article/(?P<entry_id>[0-9]+)$',views.edit_article,name='edit_article'),
]