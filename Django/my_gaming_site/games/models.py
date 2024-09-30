from django.db import models
from django.contrib.auth.models import User

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.game}: {self.score}"
