# coding=utf-8
# -*- coding:utf-8 -*-
# author:天际
# datetime:2018/5/18 22:33
# software: PyCharm
from django import forms
from .models import Article,Category,Tag

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name']
		labels = {'name': ''}

class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = ['name']
		labels = {'name': ''}

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['title','body','excerpt','category','tag','author']
		labels = {'title': '题目','body': '内容','category': '类别','tag': '标签',
		          'excerpt': '摘要','author': '作者'}
		widgets = {'title': forms.TextInput(),'body': forms.Textarea(attrs={'cols' : 80}),'category': forms.Select(),
		           'tag': forms.CheckboxSelectMultiple(),'excerpt': forms.Textarea(attrs={'cols' : 20}),'author': forms.Select()}
