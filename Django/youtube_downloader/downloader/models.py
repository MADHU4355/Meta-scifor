from django.db import models
from django.contrib.auth.models import User

class Download(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='downloads')
    video_title = models.CharField(max_length=255)
    video_url = models.URLField()
    download_date = models.DateTimeField(auto_now_add=True)
    file_path = models.CharField(max_length=255)  # Path where the file is saved

    def __str__(self):
        return f"{self.video_title} downloaded by {self.user.username} on {self.download_date}"

class FavoriteVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    video_title = models.CharField(max_length=255)
    video_url = models.URLField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.video_title} favorited by {self.user.username} on {self.added_date}"
