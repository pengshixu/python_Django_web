from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    typelist=TypeInfo.objects.all()
    type0=typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    uname = request.session.get('user', '未登录')
    context = {'uname': uname, 'type0':type0, 'type01':type01,
               'type1':type1, 'type11':type11,
               'type2':type2, 'type21':type21,
               'type3':type3, 'type31':type31,
               'type4':type4, 'type41':type41,
               'type5':type5, 'type51':type51,}
    return render(request, 'df_goods/index.html', context)

def detail(request):
    uname = request.session.get('user', '未登录')
    context = {'uname': uname}
    return render(request, 'df_goods/detail.html', context)

def list(request):
    uname = request.session.get('user', '未登录')
    context = {'uname': uname}
    return render(request, 'df_goods/list.html', context)