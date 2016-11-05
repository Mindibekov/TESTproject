# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
import HRONION.views as views


urlpatterns = [ 
	url(r'^start/register/', views.register),
	url(r'^start/', views.start),
]