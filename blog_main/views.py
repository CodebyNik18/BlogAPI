from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Blog

def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request=request, template_name='home.html', context=context)