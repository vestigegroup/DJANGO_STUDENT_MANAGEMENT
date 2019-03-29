from datetime import date
from django.shortcuts import render
from teachers.models import Teacher, TeacherInfo, TeacherQualification


def index(request):
    teachers = Teacher.objects.order_by('techer_id')        # '-techer_id' for ascending order
    context = {
        'teachers': teachers,
    }
    return render(request, 'teachers/teacher_index.html', context)


def teacher_detail(request, teacher_id):
    instructor = Teacher.objects.get(pk=teacher_id)
    details = TeacherInfo.objects.get(pk=teacher_id)

    def age(dob):
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    instructorAge = age(details.dateOfBirth)
    qualifications = TeacherQualification.objects.all()
    context = {
        'instructor': instructor,
        'details': details,
        'instructorAge': instructorAge,
        'qualifications': qualifications,
    }
    return render(request, 'teachers/detail.html', context)