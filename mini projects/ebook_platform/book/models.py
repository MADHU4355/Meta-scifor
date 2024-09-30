from django.db import models

class Ebook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='ebooks/')

    def __str__(self):
        return self.title

class Poster(models.Model):
    title = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title
    
class BusinessCard(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='business_cards/')

    def __str__(self):
        return self.name
