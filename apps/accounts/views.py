from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.contrib.auth import authenticate, login

# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, logout


from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def dashboard(request):
    content = "Big big BOOBIES!!!"
    return render(request, "accounts/dashboard.html", {"content":content} )
    # return HttpResponse("Hi there Dashboard Dude")

def login_page(request):
    # return HttpResponse("I am the Login Master")
    content = "Big big WEINERS!!!"
    context = {
        "content":content,
    }
    return render(request, 'accounts/login_page.html', context)


def register_page(request):
    # return HttpResponse("I am the Register with the most")
    content = "BOOBIES and WEINERS!!!"
    context = {
        "content":content,
    }
    return render(request, 'accounts/register_page.html', context)
