from django.shortcuts import render
from rest_framework import generics
from blogs.models import Comment, Blog
from .serializers import BlogSerializer, CommentSerializer

class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer