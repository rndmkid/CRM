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
from accounts.forms import CustomAuthenticationForm
from contacts import views as contact_views

urlpatterns = [
    #path('admin/', admin.site.urls),

   # Marketing pages
    url(r'^$', HomePage.as_view(), name="home"),

    # Subscriber related URLs
    url(r'^signup/$', sub_Views.subscriber_new, name='sub_new'),

    # Admin URL
    url('^admin/', admin.site.urls),

    # Login/Logout URLs
    url(r'^login/$',
        LoginView.as_view(template_name="login.html",
                          authentication_form=CustomAuthenticationForm,
                          ),
        name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page="/login/")),

    # Account related URLs
    url('^account/', include('accounts.urls')),
    
    # Contact related URLS
    url(r'^contact/new/$', contact_views.contact_create, name='contact_new'),
    url(r'^contact/(?P<uuid>[\w-]+)/', include('contacts.urls')),

    # Communication related URLs
]
