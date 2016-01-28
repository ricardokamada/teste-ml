# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include


urlpatterns = patterns('graph.views',
	url(r'^$', 'graph', name='graph'),    
)