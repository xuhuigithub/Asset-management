"""cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from . import host
from hostinfo import views as hostinfo_views
from userinfo import views as userinfo_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hostinfo$',host.get_all),
    url(r'^update$',host.update_one),
    url(r'^table$',hostinfo_views.index),
    url(r'^add_host$',hostinfo_views.Add_test),
    url(r'^del_host$',hostinfo_views.Delete),
    url(r'^update_host$',hostinfo_views.Update),
    url(r'^user_login$', userinfo_views.Login),
    url(r'^test_login$', userinfo_views.Login_t),
    url(r'^login$', userinfo_views.Login_g),
    url(r'^test_logout$', userinfo_views.Logout_t),
    url(r'^user_logout$', userinfo_views.Logout),
]
