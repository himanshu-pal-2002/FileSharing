from rest_framework import serializers
from .models import *

class FileListSerializer(serializers.Serializer):

    files = serializers.ListField(
        child = serializers.FileField(max_length = 100000, allow_empty_file = False, use_url = False)
    )

    def create(self, validate_data):

        folder = Folder.objects.create()