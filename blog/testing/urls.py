from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.testing, name="testing-testing"),
    path("images/", views.ImageCreateView.as_view(), name="image-create"),
]
