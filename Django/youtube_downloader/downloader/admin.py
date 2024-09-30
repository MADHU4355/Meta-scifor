from django.contrib import admin
from .models import Download, FavoriteVideo

class DownloadAdmin(admin.ModelAdmin):
    list_display = ('user', 'video_title', 'download_date')
    search_fields = ('video_title', 'user__username')
    list_filter = ('download_date',)

class FavoriteVideoAdmin(admin.ModelAdmin):
    list_display = ('user', 'video_title', 'added_date')
    search_fields = ('video_title', 'user__username')
    list_filter = ('added_date',)

admin.site.register(Download, DownloadAdmin)
admin.site.register(FavoriteVideo, FavoriteVideoAdmin)


#madhu. HKMytd@16