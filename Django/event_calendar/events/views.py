from django.shortcuts import render
from .models import Event
from django.utils import timezone

def event_list(request):
    events = Event.objects.filter(start_time__gte=timezone.now()).order_by('start_time')
    return render(request, 'events/events_list.html', {'events': events})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/events_detail.html', {'event': event})
