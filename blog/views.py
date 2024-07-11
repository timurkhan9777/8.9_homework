from django.shortcuts import render
from .models import Category,Post,Comment,Like
from .serializers import CommentSerializer,PostSerializer,CategorySerializer,LikeSerializer
from .permissions import CustomPermission
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication


class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermission]
    authentication_classes = [BasicAuthentication,SessionAuthentication]

class PostAPIView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [CustomPermission]
    authentication_classes = [TokenAuthentication]

class CommentAPIView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CustomPermission]

class LikeAPIView(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [CustomPermission]