__author__ = 'csy'

from django.conf.urls import patterns, include, url

import  views

urlpatterns = patterns('',

    url(r'^$',views.index),
    url(r'^detail/(\d+)/$', views.blog_detail),
    url(r'^blogcategory/(\d+)/$',views.blog_category),
    url(r'^download/',views.download),
    url(r'^about/', views.about),
    url(r'^downloadcategory/(\d+)/$',views.download_category),
)