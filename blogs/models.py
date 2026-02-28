from django.db import models


class Blog(models.Model):
    blog_title = models.CharField(max_length=500)
    blog_body = models.TextField()
    images = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_body[:100]
    
    
class Comment(models.Model):
    blog = models.ForeignKey(to=Blog, on_delete=models.CASCADE, related_name='comments')
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog.blog_body[:100]