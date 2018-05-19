from django.contrib import admin
from .models import Category,Tag,Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title','created_time','modified_time','category','author']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
