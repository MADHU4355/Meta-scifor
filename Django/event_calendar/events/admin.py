from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'created_at')
    list_filter = ('start_time', 'end_time')
    search_fields = ('title', 'description')


#madhu, kiranmadhu4355@gmail.com, HKMevents@16