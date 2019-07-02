# from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from df_cart.models import *
from df_goods.models import *
from df_user.models import *
from django.http import HttpResponse, JsonResponse
from . import user_decorator
from django.core.paginator import Paginator
from django.db import transaction
from datetime import datetime
from decimal import Decimal

# Create your views here.
@user_decorator.login
def place_order(request):
    uname = request.session.get('user', '未登录')
    id = request.session.get('id', 'null')
    cart_user = UserInfo.objects.get(id=id)
    cart_id = request.GET.getlist('cart_id')
    carts = CartInfo.objects.filter(id__in=cart_id)
    context = {'uname': uname, 'carts':carts, 'cart_user':cart_user}
    return render(request, 'df_order/place_order.html', context)

'''
事务：一旦操作失败则全部回退
1、创建订单对象
2、判断商品的库存
3、创建详单对象
4、修改商品库存
5、删除购物车
'''

@transaction.atomic()
@user_decorator.login
def order_handle(request):
    tran_id = transaction.savepoint()
    #购物车id
    cart_ids = request.POST.getlist('cart_id')
    print(cart_ids)
    try:
        #创建订单对象
        order = OrderInfo()
        now = datetime.now()
        uid = request.session['id']
        user = UserInfo.objects.get(id = uid)
        order.oid = '%s%d'%(now.strftime('%Y%m%d%H%M%S'),uid)
        order.user_id = uid
        order.odate = now
        order.ototal = request.POST.get('ototal')
        order.oaddress = user.uaddress
        order.save()
        for cart_id in cart_ids:
            detail = OrderDetailInfo()
            detail.order = order
            cart = CartInfo.objects.get(id = cart_id)
            goods = cart.goods
            if goods.gkucun >= cart.count:
                goods.gkucun = cart.goods.gkucun - cart.count
                goods.save()
                detail.goods_id = goods.id
                detail.price = goods.gprice
                detail.count = cart.count
                detail.save()
                cart.delete()
            else:
                transaction.savepoint_rollback(tran_id)
                return redirect('/cart/')
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print('==============%s'%e)
        transaction.savepoint_rollback(tran_id)
    return redirect('/order/order_1')

@user_decorator.login
def order(request, pindex):
    uname = request.session.get('user', '未登录')
    uid = request.session.get('id', 'null')
    cart_id = request.POST.getlist('cart_id')
    cart_user = UserInfo.objects.get(id=uid)
    orders = cart_user.orderinfo_set.all().order_by('-odate')
    paginator = Paginator(orders, 2)
    page = paginator.page(int(pindex))
    cart_ids = []
    for c_id in cart_user.orderinfo_set.all().values('oid'):
        cart_ids.append(list(c_id.values())[0])
        # print(cart_ids)
    details = OrderDetailInfo.objects.filter(order__in=cart_ids)
    context = {'uname': uname, 'orders': orders, 'details': details, 'page':page, 'paginator':paginator}
    return render(request, 'df_order/user_center_order.html', context)