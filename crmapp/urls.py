"""crmapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from marketing.views import HomePage
from subscribers import views as sub_Views
#from accounts import views as acc_Views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    #path('admin/', admin.site.urls),

   # Marketing pages
    url(r'^$', HomePage.as_view(), name="home"),

    # Subscriber related URLs
    url(r'^signup/$', sub_Views.subscriber_new, name='sub_new'),

    # Admin URL
    url('^admin/', admin.site.urls),

    # Login/Logout URLs
    url(r'^login/$', LoginView.as_view(template_name="login.html"), name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page="/login/")),

    # Account related URLs
    url('^account/', include('accounts.urls')),
##    url(r'^account/new/$', acc_Views.account_cru, name='account_new'),
##    url(r'^account/list/$',
##            acc_Views.AccountList.as_view(),
##            name='account_list'),
##    url(r'^account/(?P<uuid>[\w-]+)/', include('accounts.urls')),
##    url(r'^account/(?P<uuid>[\w-]+)/',
##            acc_Views.account_detail,
##            name='account_detail'),
    
    # Contact related URLS


    # Communication related URLs
]
