from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'homepage_sheet.html')

def aboutpage(request):
    return render(request, 'about_sheet.html')

def contactpage(request):
    return render(request, 'contact_sheet.html')