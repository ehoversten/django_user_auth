from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def dashboard(request):
    return HttpResponse("Hi there Dashboard Dude")
    
def login_page(request):
    return HttpResponse("I am the Login Master")


def register_page(request):
    return HttpResponse("I am the Register with the most")
