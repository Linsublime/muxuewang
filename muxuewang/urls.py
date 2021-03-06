"""muxuwang URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.views.generic import TemplateView
import xadmin

from users.views import Login, Register, ActiveUser, ForgetPassword, ResetPassword
from muxuewang.settings import MEDIA_ROOT


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^$', TemplateView.as_view(template_name='users/index.html'), name='index'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUser.as_view(), name='active_user'),
    url(r'^forget/$', ForgetPassword.as_view(), name='forget_password'),
    url(r'^reset/(?P<reset_code>.*)/$', ResetPassword.as_view(), name='reset_password'),

    url(r'^org/', include('organizations.urls', namespace='org')),

    url(r'^course/', include('courses.urls', namespace='course')),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
