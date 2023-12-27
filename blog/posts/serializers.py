from . import models
from rest_framework import serializers
from users.serializers import BlogUserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class PostDetailsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = BlogUserSerializer()

    class Meta:
        model = models.Post
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = "__all__"


class CommentDetailsSerializer(serializers.ModelSerializer):
    user = BlogUserSerializer()

    class Meta:
        model = models.Comment
        fields = "__all__"
