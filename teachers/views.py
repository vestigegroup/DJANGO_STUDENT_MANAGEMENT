from django.shortcuts import render


def index(request):
    return render(request, 'teachers/teacher_index.html')
