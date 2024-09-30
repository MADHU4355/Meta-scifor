from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Ebook, Poster

@admin.register(Ebook)
class EbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'uploaded_at')
    search_fields = ('title', 'author')

@admin.register(Poster)
class PosterAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)
