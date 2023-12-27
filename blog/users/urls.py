from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ListUsersView.as_view(), name="Get all users"),
    path("<int:pk>", views.GetUserView.as_view(), name="Get single user"),
    path("create-account", views.CreateAccountView.as_view(), name="Create account"),
    path("login", views.LogInView.as_view(), name="Login user"),
    path("logout", views.LogOutView.as_view(), name="Logout user"),
    path("update/<int:pk>", views.UpdateUserView.as_view(), name="Update user"),
    path(
        "update-profile-image/<int:pk>",
        views.UpdateUserProfileImageView.as_view(),
        name="Update user profile image",
    ),
    path("delete/<int:pk>", views.DeleteUserView.as_view(), name="Delete user"),
]
