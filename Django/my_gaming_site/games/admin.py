from django.contrib import admin
from .models import Score

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'score')
    search_fields = ('user__username', 'game')

admin.site.register(Score, ScoreAdmin)
