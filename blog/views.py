from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Post,Category,Comment
from .serializers import PostSerializer,CategorySerializer,CommentSerializer
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostDateView(viewsets.ModelViewSet):
    posts = Post.objects.order_by('-published_date')
    serializer_class = PostSerializer

class PostPopularView(viewsets.ModelViewSet):
    posts = Post.objects.filter(is_popular=True)
    serializer_class = PostSerializer

class PostRecommendedView(viewsets.ModelViewSet):
    posts = Post.objects.filter(is_recommended=True)
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination

class PostDetailView(viewsets.ModelViewSet):
    posts = Post.objects.all()
    serializer_class=PostSerializer

class PostReadNextView(viewsets.ModelViewSet):
    posts = Post.objects.filter(is_read_next=True)
    serializer_class= PostSerializer


class CommentView(viewsets.ModelViewSet):
    comment = Comment.objects.all()
    serializer_class=CommentSerializer