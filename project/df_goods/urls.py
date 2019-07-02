from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^index/$', views.index),
    url(r'^detail/(\d+)/$', views.detail),
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.list)
]