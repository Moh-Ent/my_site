from django.urls import path
from blog.views import * 

app_name = 'blog'

urlpatterns = [
    path('', bloghomepage, name = 'blogindexURL'),
    path('single/', blogdetailpage, name = 'blogdetailURL'),
]