from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Blog, Comment

def addPost(request):
    return render(request=request, template_name='add_post.html')

def postDetail(request, pk):
    blog = Blog.objects.get(pk=pk)
    comments = Comment.objects.filter(blog=pk)
    context = {
        'blog': blog,
        'comments': comments
    }
    return render(request=request, template_name='post_details.html', context=context)