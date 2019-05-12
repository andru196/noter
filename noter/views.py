from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout
from django.http import HttpResponseRedirect
from .models import *
from django.forms.models import model_to_dict
from .form import *
from django.http import HttpResponse
import json
from datetime import date


def get_note(request):
    note = request.GET.get('id')
    note = Note.objects.get(id=note)
    if note.user == request.user:
        return HttpResponse(json.dumps(model_to_dict(note)))
    return  HttpResponse("!KO!")


def del_note(request):
    note = request.GET.get('id')
    note = Note.objects.get(id=note)
    if note.user == request.user and not note.locked:
        note.deleted = date.today()
        note.save()
        return HttpResponse("OK")
    else:
        return HttpResponse("!KO!")


def locker(request):
    note = request.GET.get('id')
    note = Note.objects.get(id=note)
    if note.locked and note.user == request.user:
        note.locked = False
    elif not note.locked and note.user == request.user:
        note.locked = True
    note.save()
    return HttpResponse(note.locked.__str__())


def index(request):
    if request.user.is_authenticated == False:
        return HttpResponseRedirect("login/")
    if request.method == "POST":
        n_id = request.POST.get('id')
        if n_id == "NEW":
            note = Note()
            note.user = request.user
        else:
            note = Note.objects.get(id=n_id)
            if note.user != request.user:
                return logout(request)
            if note.locked == True:
                return HttpResponseRedirect('/')
        text = request.POST.get("text")
        note.text = text
        note.color = request.POST.get('color')
        note.shorttext = (text[0:49].replace("<br>", "\n").split('\n'))[0]
        note.save()
        return HttpResponseRedirect('/')
    notes = Note.objects.filter(user=request.user, deleted=None).values("id", "shorttext", 'color')
    if notes.count() == 0:
        notes = {"id": "0", "shorttext": "Нет заметок"}
    return render(request, "noter/index.html", {"notes": notes, "form": SaveForm(), "form1": IDForm()})


def login(request, log=""):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    if log != '':
        logs = ["Сперва авторизиуйтесь","Вы успешно вышли"]
        log = logs[int(log) - 1]
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("login")
        else:
            log = "Введена не правильная пара логин-пароль"
    userform = LogForm()
    return render(request, "noter/regit.html", {"form": userform, "log": log, "name": "Авторизация"})


def regist(request, log=""):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    if log != '':
        logs = ["Имя пользователя используется", "Email используется"]
        log = logs[int(log) - 1]
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        if User.objects.filter(username=username).count() > 0:
            return HttpResponseRedirect("/reg/1")
        if User.objects.filter(email=email).count() > 0:
            return HttpResponseRedirect("/reg/2")
        user = User.objects.create_user(username, email, password)
        auth_login(request, user)
        return HttpResponseRedirect("list")
    else:
        regform = RegForm()
        return render(request, "noter/regit.html", {"form": regform, "log": log, "name": "Регистрация"})


def log_out(request):
    logout(request)
    return HttpResponseRedirect("login/2")