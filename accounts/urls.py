from django.urls import path
from django.conf.urls import url, include
from accounts import views

urlpatterns = [
    url(r'^account/new/$', views.account_cru, name='account_new'),
    url(r'^account/list/$',
            views.AccountList.as_view(),
            name='account_list'),
    url(r'^account/(?P<uuid>[\w-]+)/', include('accounts.acc_urls')),
]

