from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializers


class BlogView(APIView):
    # Class for view the published posts; Just the 5 latest published posts
    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(
            status='published').order_by('-published')[:5]
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)
    

class BlogDetailView(APIView):
    # Class for view an specific post by slug
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'])
        serializer = PostSerializers(post)
        return Response(serializer.data)
