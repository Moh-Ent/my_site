from django.shortcuts import render

# Create your views here.
def bloghomepage(request):
    return render(request, 'blog/blog-home.html')

def blogdetailpage(request):
    return render(request, 'blog/blog-single.html')