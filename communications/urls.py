from django.urls import path
from django.conf.urls import include, url
from . import views

comm_urls = [
    url('^$', views.comm_detail, name="comm_detail"),
    url('^edit/$',views.comm_cru, name='comm_update'),
]

urlpatterns = [
    #url(r'(?P<uuid>[\w-]+)/', views.comm_detail, name="comm_detail"),
    url('', include(comm_urls)),
]


