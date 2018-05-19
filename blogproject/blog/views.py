from django.shortcuts import render,get_object_or_404
from .models import Article,Category
from django.views.generic import ListView,DetailView
from .forms import CategoryForm,TagForm,ArticleForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import markdown
# Create your views here.
def index(request):
    article_list = Article.objects.all().order_by("-created_time")
    context = {"article_list":article_list}
    return render(request,'blog/index.html',context=context)
# 分页选项在下面的这个视图中
class IndexView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        pagination_data = self.pagination_data(paginator,page,is_paginated)
        context.update(pagination_data)
        return  context

    def pagination_data(self,paginator,page,is_paginated):
        if not is_paginated:
            return {}
        left = []
        right = []
        left_has_more = True
        right_has_more = True
        first = False
        last = False
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range

        if page_number == 1:
            right = page_range[page_number:page_number+2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] >1:
                first = True
        else:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number+2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True

        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
        }

        return data
#--------------------------------------------------------#
def archives(requset,year,month):
    article_list = Article.objects.filter(
            created_time__year = year,
            created_time__month = month
        ).order_by("-created_time")
    context = {'article_list': article_list}
    return render(requset,'blog/index.html',context=context)

class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year = year,
                                                               created_time__month = month)
#----------------------------------------------------#
def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    article_list = Article.objects.filter(category = cate).order_by('-created_time')
    context = {'article_list':article_list}
    return render(request,'blog/index.html',context=context)

class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)
#----------------------------------------------------#
def detail(request,pk):
    article = get_object_or_404(Article,pk=pk)
    article.increase_views()
    context = {
        'article': article,
    }
    return render(request,'blog/detail.html',context=context)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get(self, request, *args, **kwargs):
        response = super(ArticleDetailView,self).get(request,*args,**kwargs)
        self.object.incerase_views()
        return response

    def get_object(self, queryset=None):
        article = super(ArticleDetailView,self).get_object(queryset=None)
        return article
#---------------------------------------------------------#
def new_category(request):
    if request.method != "POST":
        form = CategoryForm()
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:index'))
    context = {'form': form}
    return render(request,'blog/new_category.html',context)
#---------------------------------------------------------#
def new_tag(request):
    if request.method != "POST":
        form = TagForm()
    else:
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:index'))
    context = {'form': form}
    return render(request,'blog/new_tag.html',context)
#---------------------------------------------------------#
def new_article(request):
    if request.method != 'POST':
        form = ArticleForm()
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            new_atricle = form.save(commit=False)
            new_atricle.save()
            return HttpResponseRedirect(reverse('blog:index'))
    print("end")
    context = {'form': form}
    return render(request,'blog/new_article.html',context)
#---------------------------------------------------------#
#def edit_article(request,entry_id):
#    article =