from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from . import user_decorator
# 相对导入的时候不能返回到顶层目录去导入，否则会报错。

# Create your views here.
@user_decorator.login
def cart(request):
    uid=request.session['id']
    uname = request.session.get('user', '未登录')
    carts=CartInfo.objects.filter(user_id=uid)
    context={
        'uname':uname,
        'title':'购物车',
        'page_num':1,
        'carts':carts
    }
    return render(request,'df_cart/cart.html',context)

# @user_decorator.login
# def cart(request):
#     uname = request.session.get('user', '未登录')
#     uid = request.session['id']
#     context = {'uname': uname}
#     return render(request, 'df_cart/cart.html', context)

@user_decorator.login
def add(request, gid, count):
    uid = request.session['id']
    gid = int(gid)
    count = int(count)
    # 查询购物车中是否存在商品，有则数量增加，否则新增
    cart = CartInfo.objects.filter(user_id=uid, goods_id=gid)

    if len(cart)>=1:
        cart=cart[0]
        cart.count=cart.count+count
    else:
        cart=CartInfo()
        cart.user_id=uid
        cart.goods_id=gid
        cart.count=count
    cart.save()
    if request.is_ajax():
        count=CartInfo.objects.filter(user_id=request.session['user_id']).count()
        return JsonResponse({'count': count})
    else:
        return redirect('/cart/')

def edit(requset, gid, count):
    try:
        cart=CartInfo.objects.get(pk=int(gid))
        count1=cart.count=int(count)
        cart.save()
        data={'ok':0}
    except Exception as e:
        data={'ok':count1}
    return JsonResponse(data)

def delete(request, gid):
    try:
        cart=CartInfo.objects.get(pk=int(gid))
        cart.delete()
        data={'ok':0}
    except Exception as e:
        data={'ok':1}
    return JsonResponse(data)
