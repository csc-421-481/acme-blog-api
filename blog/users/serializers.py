from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .models import BlogUser


class BlogUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogUser
        fields = (
            "id",
            "profileImage",
            "firstName",
            "lastName",
            "email",
            "matricNumber",
            "password",
            "bio",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = BlogUser.objects.create_user(**validated_data)

        # Generate and associate the token with the user
        token, created = Token.objects.get_or_create(user=user)

        return user

    def validate(self, data):
        # Ensure that username is the same as email when creating or updating the user
        data["username"] = data.get("email", data.get("username"))
        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
