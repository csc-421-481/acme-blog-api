from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import BlogUser
from .serializers import BlogUserSerializer, LoginSerializer
from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model, authenticate, login, logout


class CreateAccountView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = BlogUserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user_data = response.data
        user = get_user_model().objects.get(id=user_data["id"])
        token, created = Token.objects.get_or_create(user=user)
        token_data = {"token": token.key}
        user_data.update(token_data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class GetUserView(generics.RetrieveAPIView):
    queryset = BlogUser.objects.all()
    serializer_class = BlogUserSerializer


class ListUsersView(generics.ListAPIView):
    queryset = BlogUser.objects.all()
    serializer_class = BlogUserSerializer


class UpdateUserView(generics.UpdateAPIView):
    queryset = BlogUser.objects.all()
    serializer_class = BlogUserSerializer


class DeleteUserView(generics.DestroyAPIView):
    queryset = BlogUser.objects.all()
    serializer_class = BlogUserSerializer


class LogInView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request,
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {"token": token.key, "user": user.id}, status=status.HTTP_200_OK
            )
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class LogOutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
