#coding=utf-8
#django package
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.core.urlresolvers import reverse
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)-15s %(user)-8s %(message)s')

#myApp package
from accounts.forms import RegisterForm
# from jizhang.data_format_func import auto_gen_categories

@login_required
def index(request):
    username = 'hank'
    return render(request,"accounts/index.html",{"username":username})

def register(request):
    '''注册视图'''
    template_var={}
    form = RegisterForm()
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username, email, password)
            user.save()
            if _login(request, username, password, template_var):
                return HttpResponseRedirect("/accounts/index")
    template_var["form"]=form
    return render(request, "accounts/register.html", template_var)

def login(request):
    template_var = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if _login(request, username, password, template_var):
            try:
                tmp = request.GET['next']
                return HttpResponseRedirect(tmp)
            except Exception as e:
                return HttpResponseRedirect("/accounts/index")
        template_var.update({"username":username})
    return render(request, "accounts/login.html", template_var)

def _login(request, username, password, dict_var):
    '''登陆核心方法'''
    ret = False
    user=authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            auth_login(request,user)
            ret = True
        else:
            dict_var["error"] = u'用户'+username+u'没有激活'
    else:
        dict_var["error"] = u'用户' + username + u'不存在或密码错误'
    return ret

def logout(request):
    auth_logout(request)
    return render(request,'accounts/logout.html',)
