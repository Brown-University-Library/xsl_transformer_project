# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView


urlpatterns = patterns('',

    url( r'^v1/$',  'transformer_app.views.run_transform_v1', name='transformer_v1_url' ),

    url( r'^info/$',  'transformer_app.views.hi', name='info_url' ),

    url( r'^$',  RedirectView.as_view(pattern_name='info_url') ),

    )
