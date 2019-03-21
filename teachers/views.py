from django.shortcuts import render
from teachers.models import Teacher


def index(request):
    teachers = Teacher.objects.order_by('techer_id')        # '-techer_id' for ascending order
    context = {
        'teachers': teachers,
    }
    return render(request, 'teachers/teacher_index.html', context)


def teacher_detail(request, teacher_id):
    instructor = Teacher.objects.get(pk=teacher_id)
    context = {
        'instructor': instructor,
    }
    return render(request, 'teachers/detail.html', context)