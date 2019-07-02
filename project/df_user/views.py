# coding:utf-8
from django.shortcuts import render, redirect
from .models import *
from hashlib import sha1
from django.http import HttpResponse, JsonResponse
from . import user_decorator
# Create your views here.
def register(request):
    return render(request, 'df_user/register.html')

def register_handle(request):
    #接收
    post=request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    ucpwd = post.get('cpwd')
    uemail = post.get('email')
    print(uname)
    #判断
    if upwd != ucpwd:
        return redirect('/user/register/')
    #密码加密
    s1 = sha1()
    s1.update(upwd.encode("utf8"))  # 指定编码格式，否则会报错
    upwd3 = s1.hexdigest()

    #创建对象
    user=UserInfo()
    user.uname=uname
    user.upwd=upwd3
    user.uemail=uemail
    user.save()
    #转到登录页
    return redirect('/user/login/')

def register_exist(request):
    uname = request.GET.get('uname')
    count=UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def login(request):
    uname = request.COOKIES.get('uname','')
    context={'uname': uname}
    return render(request, 'df_user/login.html', context)

def login_username(request):
    #接收
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})

def login_handle(request):
    uname = request.POST.get('username')
    print(uname)
    remember = request.POST.get('remember', 0)
    print(remember)
    if(UserInfo.objects.filter(uname=uname).count() > 0):
        id=UserInfo.objects.get(uname=uname).id
        request.session['id'] = id
    request.session['user'] = uname
    request.session.set_expiry(0)
    url=request.COOKIES.get('url','/user/user_center_info/')
    red = redirect(url)
    print(remember!=0)
    if remember != 0:
        red.set_cookie('uname', uname)
    else:
        red.set_cookie('uname','',max_age=-1)
    return red

def login_pwd(request):
    uname = request.GET.get('uname')
    upwd = request.GET.get('upwd')
    # 密码加密
    s1 = sha1()
    s1.update(upwd.encode("utf8"))  # 指定编码格式，否则会报错
    upwd3 = s1.hexdigest()
    count = UserInfo.objects.filter(uname=uname, upwd=upwd3).count()
    return JsonResponse({'count': count})

@user_decorator.login
def user_center_info(request):
    uname = request.session.get('user', '未登录')
    id = request.session.get('id', 'null')
    uphone = UserInfo.objects.get(id=id).uphone
    uaddress = UserInfo.objects.get(id=id).uaddress
    context = {'uname': uname, 'uphone': uphone, 'uaddress':uaddress}
    return render(request,'df_user/user_center_info.html',context)

# def user_center_order(request):
#     uname = request.session.get('user', '未登录')
#     context = {'uname': uname}
#     return render(request, 'df_user/user_center_order.html', context)

def user_center_site(request):
    uname = request.session.get('user', '未登录')
    id = request.session.get('id', 'null')
    user = UserInfo.objects.get(id=id)
    if (request.method == 'POST'):
        post = request.POST
        ushou = post.get('ushou')
        uaddress = post.get('uaddress')
        uyoubian = post.get('uyoubian')
        uphone = post.get('uphone')
        user.ushou = ushou
        user.uaddress = uaddress
        user.uyoubian = uyoubian
        user.uphone = uphone
        user.save()
    uphone = user.uphone
    uaddress = user.uaddress
    ushou = user.ushou
    uyoubian = user.uyoubian
    context = {'uname': uname, 'uphone': uphone, 'uaddress': uaddress, 'ushou':ushou, 'uyoubian':uyoubian}
    return render(request, 'df_user/user_center_site.html', context)

# @user_decorator.login
# def cart(request):
#     uname = request.session.get('user', '未登录')
#     context = {'uname': uname}
#     return render(request, 'df_user/cart.html', context)

# @user_decorator.login
# def place_order(request):
#     uname = request.session.get('user', '未登录')
#     id = request.session.get('id', 'null')
#     user = UserInfo.objects.get(id=id)
#     uaddress = user.uaddress
#     context = {'uname': uname,'uaddress': uaddress}
#     return render(request, 'df_user/place_order.html', context)


def logout(request):
    request.session.flush()
    return redirect('/goods/index/')