from django.shortcuts import render

from django.http import HttpResponse

def user(request):
    return HttpResponse('<h1>This is User Page</h1>')
