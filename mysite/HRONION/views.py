# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import os, sys
from django.contrib import auth
from django.http import Http404, HttpResponse 

import HRONION.models as models 

from django.contrib import auth


import HRONION.bot_inform as bot_inform #  информация в месенджере телеграмм: bot_inform.sent_to_atknin_bot(massage, telegram_whom)

telegram_whom = "both"#v - ваня d - дима, остальное любое вдоем
# Create your views here.
def start(request):
	if request.method == "POST":
		name = request.POST["login"]
		password = request.POST["password"]
		user = auth.authenticate(username=name, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			return render(request, 'html/start.html')
		else:
			her = 'Не правильные данные для: ' + name
			return render(request, 'html/start.html', {'her': her})
			print("Ой, что-то пошло не так!")


		# bot_inform.sent_to_atknin_bot(user+" " + password, telegram_whom)
	else:

		massage = 'Еще одна попытка'
		# bot_inform.sent_to_atknin_bot(massage, telegram_whom)
		return render(request, 'html/start.html')

def register(request):
	if request.method == "POST":
		last_name = request.POST["Фамилия"]
		first_name = request.POST["Имя"]
		middle_name = request.POST["Отчество"]
		email = request.POST["email"]
		password = request.POST["пароль"]
		conf_password = request.POST["Подтвердите пароль"]
	return render(request, 'html/registration_form.html')	