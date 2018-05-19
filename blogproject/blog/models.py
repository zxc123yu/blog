from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Article(models.Model):
	# 文章标题
	title = models.CharField(max_length=70)
	# 文章正文
	body = models.TextField()
	#创建与修改时间
	created_time = models.DateTimeField(auto_now_add=True)
	modified_time = models.DateTimeField(auto_now_add=True)
	# 文章摘要
	excerpt = models.CharField(max_length=200,blank=True)
	# 分类与标签
	category = models.ForeignKey(Category)
	tag = models.ManyToManyField(Tag,blank=True)
	# 文章作者
	author = models.ForeignKey(User)
	# 阅读数量数
	views = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['-created_time']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})

	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])

	def save(self,*args,**kwargs):
		if not self.excerpt:
			self.excerpt = strip_tags(self.body)[:54]
		super(Article,self).save(*args,**kwargs)