# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url
from .views import get_action_records


urlpatterns = patterns(
    '',
    url(
        r'^records$',
        get_action_records,
        name='get-action-records'
    ),
)
