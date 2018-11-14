from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.contact_detail, name="contact_detail"),
    url(r'^edit/$', views.contact_cru, name='contact_update'),
    
]

