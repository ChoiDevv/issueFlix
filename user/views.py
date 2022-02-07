from http.client import HTTPResponse
from django.shortcuts import render, redirect
from user.models import UserModel
from django.contrib import auth
from django.contrib.auth import get_user_model

def start(request):
    return render(request, 'main.html')

def sign_up(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        nickname = request.POST.get('nickname', '')

        exist_user = get_user_model().objects.filter(username=username)
        
        if exist_user:
            return render(request, 'signin.html')
        else:
            UserModel.objects.create_user(username=username, password=password, nickname=nickname)
            return redirect('/sign-in')

    elif request.method == "GET": 
        return render(request, 'signin.html')

def sign_in(request):
    if request.method == "GET":
        return render(request, 'signin.html')

    elif request.method == "POST":
        username = request.POST.get('signin_username', None)
        password = request.POST.get('signin_password', None)
        
        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/main')
        else:
            return redirect('/sign-in')