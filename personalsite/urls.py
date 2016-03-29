from django.conf.urls import url
from django.contrib import admin

from .views import (
        home,
    )

urlpatterns = [
    url(r'^$', home, name='home'),
    # url(r'^create/$', post_create, ),
    # url(r'^(?P<slug>[\w-]+)/$', post_detail, name = 'detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name= 'update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, ),
]