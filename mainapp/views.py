from django.shortcuts import redirect, render
from mainapp.models import Meeting, ToDo, EventGallery
from students.models import Student
from teachers.models import Teacher
from clubs.models import Club


def home(request):
    
    students = Student.objects.all()   #for student counter
    teachers = Teacher.objects.all()    #for teacher counter
    clubs = Club.objects.all()      #for club counter
    
    meetings = Meeting.objects.all()    #for meetings
    todos = ToDo.objects.order_by('-todo_time')     #for todo
    events = EventGallery.objects.order_by('-date')     #for events
    context = {
        'students': students,
        'teachers': teachers,
        'clubs': clubs,
        'meetings': meetings,
        'todos': todos,
        'events': events,
    }
    return render(request, 'index.html', context)


def dummy(request):
    return render(request, 'dummy.html')


def redirectView(request):
    response = redirect('/welcome/')
    return response
