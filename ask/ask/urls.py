from django.conf.urls import patterns, include, url

from django.contrib import admin

import qa.views

urlpatterns = patterns('',
                       url(r'^login/$', qa.views.test),
                       url(r'^singup/$', qa.views.test),
                       url(r'^question/(\d+)', qa.views.test),
                       url(r'^ask/$', qa.views.error),
                       url(r'^popular/$', qa.views.test),
                       url(r'^new/$', qa.views.test)
                       )