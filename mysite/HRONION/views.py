# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import os, sys
from django.contrib import auth
from django.http import Http404, HttpResponse 
from django.http import HttpRequest 
import HRONION.models as models 
from django.contrib import auth
import datetime


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
	check = 1

	if request.method == "POST":
		error = {}
		last_name = request.POST["last_name"]
		first_name = request.POST["first_name"]
		middle_name = request.POST["middle_name"]
		email = request.POST["email"]
		password = request.POST["password"]
		conf_password = request.POST["conf_password"]
		login = request.POST["login"]
		if not login:
			error["error_login"] = "Login is empty"
			check = 0
		if not password == conf_password:
			check = 0
			error["error_password"] = "Пароли не совпадают"
		if check == 1:
			new_user = models.users.objects.create(username=login)
			new_user.first_name=first_name
			new_user.last_name=last_name
			new_user.email=email
			new_user.password=password 
			new_user.save()
		return render(request, 'registration/registration_form.html', {"error":error, "POST":request.POST})	 


	return render(request, 'registration/registration_form.html')

def dashboard(request):

		return render(request, 'dashboard_base.html')

def apps(request):

		return render(request, 'dashboard/apps.html')
