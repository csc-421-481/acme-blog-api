from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "title", "image"]

        # Add validators to make the image field required

    def validate_image(self, value):
        if not value:
            raise serializers.ValidationError("Image field is required.")
        return value
