# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class users(AbstractUser):
	Institute = models.CharField(max_length=200, blank = True, null = True) 

	class Meta:
		verbose_name = u'Пользователь'
		verbose_name_plural = u'Пользователи' 

	def __unicode__(self):
		return ('%s %s') % (self.username, self.email)

class subscribers(models.Model):
	name = models.CharField(max_length=30, blank=True, null=True) 
	e_mail = models.EmailField(max_length=254, unique = True)
	ip_address = models.CharField(max_length=1000)
	sub_date = models.DateTimeField(blank=True, null=True)
	class Meta:
		ordering = ('name', )
		verbose_name = u'Подписчик'
		verbose_name_plural = u'Подписчики' 
	def __str__(self):
		return self.e_mail



