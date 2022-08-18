from django.urls import path
from .views import BlogView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('posts/', BlogView.as_view(),), # /blog/posts/
    path('posts/<slug:slug>/', BlogDetailView.as_view(),), # /blog/posts/<slug>/
]
