from django.shortcuts import render
from . import serializers, models
from rest_framework import generics


class CreateAndListCategoryView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class RetrieveUpdateDestroyCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ListPostsView(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostDetailsSerializer


class ListUserPostsView(generics.ListAPIView):
    serializer_class = serializers.PostDetailsSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return models.Post.objects.filter(user_id=user_id)


#  Posts views


class CreatePostView(generics.CreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class UpdatePostView(generics.UpdateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class DestroyPostView(generics.DestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class RetrievePostView(generics.RetrieveAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostDetailsSerializer


# Comments


class RetrieveCommentsByPostView(generics.ListAPIView):
    serializer_class = serializers.CommentDetailsSerializer

    def get_queryset(self):
        post_id = self.kwargs["post_id"]
        return models.Comment.objects.filter(post_id=post_id)


class CreateCommentByPostView(generics.CreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
