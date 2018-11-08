from django.urls import path
from django.conf.urls import url, include
from accounts import views

urlpatterns = [
    url(r'^$',
        views.account_detail, name='account_detail'
    ),
     url(r'^edit/$',
        views.account_cru, name='account_update'
    ),
    
]

