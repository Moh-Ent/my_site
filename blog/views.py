from django.shortcuts import render
from blog.models import Post

# Create your views here.
def bloghomepage(request):
    posts = Post.objects.filter(is_published=1)
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)

def blogdetailpage(request):
    return render(request, 'blog/blog-single.html')