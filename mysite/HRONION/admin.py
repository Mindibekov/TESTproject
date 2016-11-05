# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
import HRONION.models

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = (u'username', u'email', 'Institute')
class SubscribersAdmin(admin.ModelAdmin):
	list_display = ('name', 'e_mail', 'ip_address')


admin.site.register(HRONION.models.users, UserAdmin)
admin.site.register(HRONION.models.subscribers, SubscribersAdmin)
