# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
import HRONION.views

urlpatterns = [ 
	url(r'^start/', HRONION.views.start),
]