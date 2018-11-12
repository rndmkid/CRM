from django.urls import path
from django.conf.urls import url, include
from accounts import views

urlpatterns = [
    url('^new/$', views.account_create, name='account_new'),
    url('^list/$',
            views.AccountList.as_view(),
            name='account_list'),
    url('^(?P<uuid>[\w-]+)/', include('accounts.acc_urls')),
]

