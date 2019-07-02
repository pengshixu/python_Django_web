from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^place_order/$', views.place_order),
    url(r'^user_center_order/$', views.order_handle),
    url(r'^order_(\d+)/$', views.order)
]