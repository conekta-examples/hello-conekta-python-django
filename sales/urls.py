from django.conf.urls import *
from sales import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^charge/$', views.charge, name="charge"),
]
