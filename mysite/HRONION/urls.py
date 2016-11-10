# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
import HRONION.views as views


urlpatterns = [ 
	url(r'^register/', views.register),
	url(r'^start/', views.start),
	url(r'^dashboard/$', views.dashboard),
	url(r'^dashboard/apps/$', views.apps),
	url(r'^dashboard/apps/form/$', views.forms),	

]