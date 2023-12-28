from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from posts.models import Post

from .models import BlogUser


class BlogUserSerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = BlogUser
        fields = (
            "id",
            "profileImage",
            "firstName",
            "lastName",
            "isTeamMember",
            "email",
            "matricNumber",
            "password",
            "bio",
            "createdAt",
            "updatedAt",
            "posts_count",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def get_posts_count(self, user):
        return Post.objects.filter(user=user).count()

    def create(self, validated_data):
        user = BlogUser.objects.create_user(**validated_data)

        # Generate and associate the token with the user
        token, created = Token.objects.get_or_create(user=user)

        return user

    def validate(self, data):
        # Ensure that username is the same as email when creating or updating the user
        data["username"] = data.get("email", data.get("username"))
        return data


class UpdateBlogUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogUser
        fields = [
            "firstName",
            "lastName",
            "email",
            "matricNumber",
            "isTeamMember",
            "bio",
        ]


class UpdateBlogUserProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogUser
        fields = ["profileImage"]


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
