    # -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'home.html'}),
    (r'^sources/$', direct_to_template, {'template': 'codespeed/sources.html'}),
    (r'^about/$', direct_to_template, {'template': 'about.html'}),
)

urlpatterns += patterns('codespeed.views',
    (r'^changes/$', 'changes'),
    (r'^changes/table/$', 'getchangestable'),
    (r'^changes/logs/$', 'displaylogs'),
    (r'^timeline/$', 'timeline'),
    (r'^timeline/json/$', 'gettimelinedata'),
    (r'^comparison/$', 'comparison'),
    (r'^comparison/json/$', 'getcomparisondata'),
)

urlpatterns += patterns('codespeed.views',
    # URL interface for adding results
    (r'^result/add/$', 'addresult'),
)
