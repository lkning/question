from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from django.urls import reverse
from app01 import models
# from django.db import
import json
def login(request):
    if request.is_ajax():
        log = {"state":True}
        username = request.POST.get("username")
        password = request.POST.get("password")
        user =models.UserInfo.objects.filter(username=username, password=password).first()
        if user:
            # request.ge
            request.session["is_login"] = True
            request.session["user"] = user.identify
            return JsonResponse(log)
        log["state"] = False
        return  JsonResponse(log)
    return render(request,"login.html")

def logAuth(func):
    def inner(request,*args,**kwargs):
        is_login = request.session.get("is_login")
        if not is_login:
            return redirect(reverse("login"))
        else:
            return func(request)
    return inner

@logAuth
def index(request):
    questions = models.Questionnaire.objects.all()
    return render(request,"index.html",locals())


@logAuth
def addQuestionnaire(request):

    return render(request,"addQuestionnaire.html")