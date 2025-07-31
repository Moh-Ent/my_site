from django.urls import path
from .views import * 

app_name = 'base'

urlpatterns = [
    path('', homepage, name = 'indexURL'),
    path('about', aboutpage, name = 'aboutURL'),
    path('contact', contactpage, name = 'contactURL')
]