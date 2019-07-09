from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^api_goods/$', views.api_goods),
    url(r'^api_cart/$', views.api_cart),
    url(r'^api_user/$', views.api_userInfo),
    url(r'^api_goodslist_(\d+)/$', views.api_goodslist),
    url(r'^api_goodsdetail_(\d+)/$', views.api_goodsdetail),
    url(r'^api_plus_(\d+)/$', views.api_plus),
    url(r'^api_diss_(\d+)/$', views.api_diss),
    url(r'^api_edit_(\d+)_(\d+)/$', views.api_edit),
    url(r'^api_add_(\d+)/$', views.api_add)
]