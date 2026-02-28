from django.urls import path
from . import views

urlpatterns = [
    path('add_post', views.addPost, name='addPost'),
    path('post_detail/<int:pk>', views.postDetail, name='postDetail'),
]