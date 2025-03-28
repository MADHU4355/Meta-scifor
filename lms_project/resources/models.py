from django.db import models
from django.utils import timezone

class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent_folder = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subfolders')
    created_at = models.DateTimeField(auto_now_add=True)  # Only keep auto_now_add=True

    def __str__(self):
        return self.name

class Resource(models.Model):
    RESOURCE_TYPES = [
        ('blog', 'Blog'),
        ('pdf', 'PDF'),
        ('article', 'Article'),
        ('video', 'Video'),
    ]
    title = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES)
    content = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='resources/', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    folder = models.ForeignKey(Folder, related_name='resources', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
