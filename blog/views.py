from django.shortcuts import render
from .models import Blog

# Create your views here.
def all_blogs(request):
    # blog = Blog.objects.order_by('-date')
    blog = Blog.objects.all()
    return render (request,"blog/blog.html",{'blog':blog})