from django.conf.urls import include, url
from django.contrib import admin

import blog.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'jester.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', blog.views.index, name = "index"),
    url(r'^admin/', include(admin.site.urls)),
]
