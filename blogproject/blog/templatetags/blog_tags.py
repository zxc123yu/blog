# coding=utf-8
# -*- coding:utf-8 -*-
# author:天际
# datetime:2018/5/16 23:42
# software: PyCharm
# 存放自定义的模板标签代码
from django import template
from ..models import Article,Category

register = template.Library()

@register.simple_tag #最新文章
def get_recent_articles(num = 5):
	return Article.objects.all().order_by('-created_time')[:num]

@register.simple_tag #归档
def archives():
	return Article.objects.dates('created_time','month',order='DESC')

@register.simple_tag #分类数据
def get_categories():
	return Category.objects.all()
