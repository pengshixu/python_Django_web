from django.shortcuts import render, redirect
from df_cart.models import *
from df_goods.models import *
from df_goods.models import *
from df_order.models import *
from df_user.models import *
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json

# Create your views here.
def api_goods(request):
    typelist = TypeInfo.objects.all()
    typeInfo = []
    for type in typelist:
        typeInfo.append({
            'type':type.ttitle,
            'type_id':type.id,
            'goods_info':
                [
                ]
        })
        for goods in type.goodsinfo_set.order_by('-id')[0:4]:
            # print(typeInfo)
            typeInfo[-1]['goods_info'].append(
                {
                    'gid':goods.id,
                    'gtitle':goods.gtitle,
                    'gpic':str(goods.gpic),
                    'gprice':goods.gprice,
                    'gunit':goods.gunit,
                    'gjianjie':goods.gjianjie,
                    'gkucun':goods.gkucun
                    # 'gtype':goods.gtype
                }
            )
    return JsonResponse(typeInfo, safe=False)

def api_cart(request):
    uname = request.GET.get('uname')
    print(uname)
    userID = UserInfo.objects.get(uname=uname).id
    cartlist = CartInfo.objects.filter(user_id = userID)
    cartInfo = []
    for cart in cartlist:
        cartInfo.append({
            'cartID':cart.id,
            'userID':cart.user_id,
            'gtitle':cart.goods.gtitle,
            'gpic':str(cart.goods.gpic),
            'gjianjie':cart.goods.gjianjie,
            'gprice':cart.goods.gprice,
            'count':cart.count
        }
        )
    return JsonResponse(cartInfo, safe=False)

def api_userInfo(request):
    uname = request.GET.get('uname')
    print(uname)
    user = UserInfo.objects.get(uname=uname)
    userInfo = []
    userInfo.append({
        'uname':user.uname,
        'uemail':user.uemail,
        'ushou':user.ushou,
        'uaddress':user.uaddress,
        'uphone':user.uphone,
        'uyoubian':user.uyoubian
    })
    return JsonResponse(userInfo, safe=False)

def api_goodslist(request,gid):
    goods = GoodsInfo.objects.filter(gtype=gid)
    goodlist = []
    for good in goods:
        goodlist.append({
            'gid': good.id,
            'gtitle': good.gtitle,
            'gpic': str(good.gpic),
            'gprice': good.gprice,
            'gunit': good.gunit,
            'gjianjie': good.gjianjie,
            'gkucun': good.gkucun
        })
    return JsonResponse(goodlist, safe=False)

def api_goodsdetail(request, gid):
    good = GoodsInfo.objects.get(id=gid)
    goodsdetail = {
        'gid': good.id,
        'gtitle': good.gtitle,
        'gpic': str(good.gpic),
        'gprice': good.gprice,
        'gunit': good.gunit,
        'gjianjie': good.gjianjie,
        'gkucun': good.gkucun,
        'gcontent': good.gcontent
    }
    return JsonResponse(goodsdetail, safe=False)

def api_plus(request, cid):
    cart = CartInfo.objects.filter(id=cid)
    if len(cart)>=1:
        cart=cart[0]
        cart.count=cart.count+1
    else:
        cart=CartInfo()
    cart.save()
    userID = CartInfo.objects.get(id=cid).user
    cartlist = CartInfo.objects.filter(user_id=userID)
    cartInfo = []
    for cart in cartlist:
        cartInfo.append({
            'cartID': cart.id,
            'userID': cart.user_id,
            'gtitle': cart.goods.gtitle,
            'gpic': str(cart.goods.gpic),
            'gjianjie': cart.goods.gjianjie,
            'gprice': cart.goods.gprice,
            'count': cart.count
        }
        )
    return JsonResponse(cartInfo, safe=False)

def api_diss(request, cid):
    cart = CartInfo.objects.filter(id=cid)
    if len(cart)>=1:
        cart=cart[0]
        cart.count=cart.count-1
    else:
        cart=CartInfo()
    cart.save()
    userID = CartInfo.objects.get(id=cid).user
    cartlist = CartInfo.objects.filter(user_id=userID)
    cartInfo = []
    for cart in cartlist:
        cartInfo.append({
            'cartID': cart.id,
            'userID': cart.user_id,
            'gtitle': cart.goods.gtitle,
            'gpic': str(cart.goods.gpic),
            'gjianjie': cart.goods.gjianjie,
            'gprice': cart.goods.gprice,
            'count': cart.count
        }
        )
    return JsonResponse(cartInfo, safe=False)

def api_edit(request, cid, num):
    cart = CartInfo.objects.filter(id=cid)
    if len(cart) >= 1:
        cart = cart[0]
        cart.count = num
    else:
        cart = CartInfo()
    cart.save()
    userID = CartInfo.objects.get(id=cid).user
    cartlist = CartInfo.objects.filter(user_id=userID)
    cartInfo = []
    for cart in cartlist:
        cartInfo.append({
            'cartID': cart.id,
            'userID': cart.user_id,
            'gtitle': cart.goods.gtitle,
            'gpic': str(cart.goods.gpic),
            'gjianjie': cart.goods.gjianjie,
            'gprice': cart.goods.gprice,
            'count': cart.count
        }
        )
    return JsonResponse(cartInfo, safe=False)

def api_add(request, gid):
    uname = request.GET.get('uname')
    print(uname)
    uid = UserInfo.objects.get(uname=uname).id
    cart = CartInfo.objects.filter(user_id=uid, goods_id=gid)
    if len(cart) >= 1:
        cart = cart[0]
        cart.count = cart.count + 1
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = 1
    cart.save()
    cartlist = CartInfo.objects.filter(user_id=uid)
    cartInfo = []
    for cart in cartlist:
        cartInfo.append({
            'cartID': cart.id,
            'userID': cart.user_id,
            'gtitle': cart.goods.gtitle,
            'gpic': str(cart.goods.gpic),
            'gjianjie': cart.goods.gjianjie,
            'gprice': cart.goods.gprice,
            'count': cart.count
        }
        )
    return JsonResponse(cartInfo, safe=False)