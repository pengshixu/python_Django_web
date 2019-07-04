from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^api_goods/$', views.api_goods),
    url(r'^api_cart/$', views.api_cart),
    url(r'^api_user/$', views.api_userInfo),
    url(r'^api_goodslist_(\d+)/$', views.api_goodslist),
    url(r'^api_goodsdetail_(\d+)/$', views.api_goodsdetail)
]