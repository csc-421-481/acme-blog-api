from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ImageSerializer
from .models import Image

# Create your views here.


@api_view(["GET", "POST"])
def testing(request):
    return Response({"message": "what's up danger"})


class ImageCreateView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    @swagger_auto_schema(
        request_body=ImageSerializer,
        parser_classes=[MultiPartParser, FormParser],
        consumes=["multipart/form-data"],  # Specify the content type
        operation_description="Upload an image",
        operation_summary="Test the upload image feature",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
