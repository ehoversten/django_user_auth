from django.shortcuts import render, redirect, HttpResponse


def landing(request):
    return HttpResponse("You have LANDED...")
