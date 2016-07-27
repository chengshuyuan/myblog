from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import models
# Create your views here.


def index(request):
    blog_list = models.Blog.objects.all()
    for blog in blog_list:
        blog.content = ""
    author = models.Author.objects.all()
    category_list = models.BlogCategory.objects.all()
    return render_to_response('index.html', {
         'blog_list':blog_list,
         'author' : author,
         'category_list' : category_list
    })


def blog_detail(request, blog_id):
    blog = models.Blog.objects.get(id=blog_id)
    author = models.Author.objects.all()
    category_list = models.BlogCategory.objects.all()
    return render_to_response('blog_detail.html',
            {'blog':blog,
             'author':author,
             'category_list' : category_list
    })


def blog_category(request, category_id):
    blog_list = models.Blog.objects.filter(category__id=category_id)
    for blog in blog_list:
        blog.content = ""
    author = models.Author.objects.all()
    category_list = models.BlogCategory.objects.all()
    return render_to_response('index.html', {
         'blog_list':blog_list,
         'author' : author,
         'category_list' : category_list
    })


def download(request):
    download_list = models.Download.objects.all()
    category_list = models.DownloadCategory.objects.all()
    return render_to_response('download.html', {
         'download_list':download_list,
         'category_list' : category_list
    })


def download_category(request, category_id):
    download_list = models.Download.objects.filter(category__id=category_id)
    category_list = models.DownloadCategory.objects.all()
    return render_to_response('download.html', {
         'download_list':download_list,
         'category_list' : category_list
    })



