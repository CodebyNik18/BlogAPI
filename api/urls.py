from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.BlogsView.as_view(), name='blogsview'),
    path('blog/<int:pk>/', views.BlogView.as_view(), name='blogview'),
    path('comments/', views.CommentsView.as_view(), name='commentsview'),
    path('comments/<int:pk>/', views.CommentView.as_view(), name='commentview')
]