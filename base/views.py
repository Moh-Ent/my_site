from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('<h1>Whatssup?</h1>')

def aboutpage(request):
    return HttpResponse('<h1>Just a chill guy</h1>')

def contactpage(request):
    return HttpResponse('<h1>Sukoma</h1>')