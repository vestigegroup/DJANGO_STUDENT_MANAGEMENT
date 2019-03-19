from django.shortcuts import render
from mainapp.models import Meeting, ToDo, EventGallery


def home(request):
    
    meeting = Meeting.objects.all()[1:]     #for meetings
    todos = ToDo.objects.order_by('-todo_time')     #for todo
    events = EventGallery.objects.order_by('-date')     #for events
    context = {
        'meeting': meeting,
        'todos': todos,
        'events': events,
    }
    return render(request, 'index.html', context)
