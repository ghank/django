# django
django_ex
2016/11/26
src  django源代码
yunjz_prj  django学习工程 django1.10.3版本 
注：
1.10.3与1.8.3存在一定区别
<1>1.10.3不需要import patterns；
<2>patterns写法不一样。
1.10.3 
#!/usr/bin/env python
#coding= utf-8
from django.conf.urls import include, url
from django.contrib import admin
from accounts import views

admin.autodiscover()

urlpatterns = [
    url(r'^$',views.login,name='login'),
    url(r'^login',views.login,name='login'),
    url(r'^logout',views.logout,name='logout'),
    url(r'^register',views.register,name='register'),
]

1.8.3 
#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login',views.login,name='login'),
    url(r'^logout',views.logout, name='logout'),
    url(r'^register',views.register,name='register'),
)

使用coverage测试覆盖率工具
1.10.3
ImportError: Failed to import test module: jizhang.tests
shiyanlou_cs419/yunjz_prj/jizhang/tests.py", line 7
注释掉这行即可，from django.contrib.auth.models import check_password
1.8.3
运行正常


