#encoding: utf-8
from django.conf.urls import url
from django.contrib import admin

from jizhang import views

admin.autodiscover()

urlpatterns = [
    # items收支列表
    url(r'^$', views.items, name="items"),
    #编辑收支
    url(r'^(?P<pk>\d+)/edit/$', views.edit_item, name='edit_item'),
    #新建收支
    url(r'^new/$',views.new_item,name='new_item'),
    #查询收支
    url(r'^find/$',views.find_item,name='find_item'),
    #categorys分类
    url(r'^categories/$', views.categories, name='categories'),
    #某个分类下的收支列表
    url(r'^categories/(?P<pk>\d+)/$', views.show_category, name='show_category'),
    #编辑分类
    url(r'^categories/(?P<pk>\d+)/edit/$', views.edit_category, name='edit_category'),
    #新建分类
    url(r'^categories/new/$',views.new_category,name='new_category'),
    #ajax
    url(r'^ajax/autocomplete_comments/',views.autocomplete_comments),
]
