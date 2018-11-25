"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from backend.views import Auth, Post
import backend.views

urlpatterns = [
    #Admin
    url(r'^admin/', admin.site.urls, name='admin'),
    #Index
    url(r'^$', backend.views.index, name='index'),
    #Auth
    url(r'^user/$', Auth.as_view({'get': 'get_user'})),
    url(r'^login/(?P<username>\w+)/(?P<password>([\W\w]+))$', Auth.as_view({'get': 'login'})),
    url(r'^logout/$', Auth.as_view({'get': 'logout'})),
    url(r'^signUp/(?P<username>\w+)/(?P<password>([\W\w]+))/(?P<email>([\w]+@[\w]+.[\w]+))$', Auth.as_view({'post': 'signUp'})),
    url(r'^findPass/(?P<username>\w+)/(?P<email>([\w]+@[\w]+.[\w]+))', Auth.as_view({'post': 'find_pass'})),
    #Posts
    url(r'^getPosts/$', Post.as_view({'get': 'get_posts'})),
    url(r'^sendPost/(?P<content>([\W\w]+))/(?P<writer>(\w+))$', Post.as_view({'post': 'send_post'})),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
