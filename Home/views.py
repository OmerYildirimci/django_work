from django.shortcuts import render,HttpResponseRedirect
from .models import Blog
def index(req):
    blog = Blog.objects.all()
    context = {
        'blog' : blog
    }
    return render(req,'index.html',context)