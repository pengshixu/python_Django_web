from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    typelist=TypeInfo.objects.all()
    type0=typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
    print(type01[0].gtype_id)
    uname = request.session.get('user', '未登录')
    context = {'uname': uname, 'type0':type0, 'type01':type01,
               'type1':type1, 'type11':type11,
               'type2':type2, 'type21':type21,
               'type3':type3, 'type31':type31,
               'type4':type4, 'type41':type41,
               'type5':type5, 'type51':type51}
    return render(request, 'df_goods/index.html', context)

def detail(request):
    uname = request.session.get('user', '未登录')
    context = {'uname': uname}
    return render(request, 'df_goods/detail.html', context)

def list(request, tid, pindex, sort):
    uname = request.session.get('user', '未登录')

    typeinfo=TypeInfo.objects.get(pk=int(tid))
    news=typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort=='1':
        goods_list=GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    if sort=='2':
        goods_list=GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    if sort=='3':
        goods_list=GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')

    paginator=Paginator(goods_list, 10)
    page=paginator.page(int(pindex))

    context = {'uname': uname, 'title':typeinfo.ttitle,
               'page':page,
               'paginator':paginator,
               'typeinfo':typeinfo,
               'sort':sort,
               'news':news}
    return render(request, 'df_goods/list.html', context)

def detail(request, id):
    uname = request.session.get('user', '未登录')
    goods=GoodsInfo.objects.get(pk=int(id))
    goods.gclick=goods.gclick+1
    goods.save()
    news=goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context={'uname': uname, 'title':goods.gtype.ttitle, 'guest_cart':1,
             'g':goods, 'news':news, 'id':id}
    return render(request, 'df_goods/detail.html', context)