from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^index/$', views.index),
    url(r'^detail/$', views.detail),
    url(r'^list/$', views.list)
]