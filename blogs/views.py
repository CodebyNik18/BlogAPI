from django.shortcuts import render
from django.http import HttpResponse

def addPost(request):
    return render(request=request, template_name='add_post.html')