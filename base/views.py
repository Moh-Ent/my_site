from django.shortcuts import render

def homepage(request):
    return render(request, 'base/index.html')

def aboutpage(request):
    return render(request, 'base/about.html')

def contactpage(request):
    return render(request, 'base/contact.html')