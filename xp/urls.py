# coding: utf-8

from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib.auth.decorators import login_required
from django.contrib import admin
admin.autodiscover()
admin.site.login = login_required(admin.site.login) # 设置admin登录的页面，settings.LOGIN_URL


urlpatterns = patterns('',

    url(r'^', include('forum.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
