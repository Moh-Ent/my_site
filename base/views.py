from django.shortcuts import render

def homepage(request):
    return render(request, 'base/homepage_sheet.html')

def aboutpage(request):
    return render(request, 'base/about_sheet.html')

def contactpage(request):
    return render(request, 'base/contact_sheet.html')