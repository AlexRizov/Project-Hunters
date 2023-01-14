from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.
def index(request):
    #user = User.objects.create_user(username = 'peter', email = 'peter@gmail.com', password = 'peterpass')
    return render(request, 'index.html')
def registration_page(request):
    return render(request, 'registration.html')
def registrate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user =  User.objects.create_user(username = username, password = password)
    return redirect(login_page)
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username, password = password)
    print(user)
    if user is not None:
        auth_login(request, user)
        return redirect(index)
    else:
        return HttpResponse('Error')
def login_page(request):
    return render(request, 'login.html')
def logout_page(request):
    auth_logout(request)
    return redirect(index)