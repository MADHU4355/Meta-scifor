from rest_framework import serializers
from .models import Folder, Resource

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ['id', 'name', 'parent_folder', 'created_at']


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'folder', 'resource_type', 'title', 'content', 'file', 'video_link', 'created_at']

    #folder = FolderSerializer()