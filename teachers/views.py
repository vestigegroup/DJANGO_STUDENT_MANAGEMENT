from datetime import date
from django.shortcuts import render, redirect
from teachers.models import Teacher, TeacherInfo, TeacherQualification
from .forms import AddTeacherForm


# Index view
def index(request):
    teachers = Teacher.objects.order_by('techer_id')        # '-techer_id' for ascending order
    context = {
        'teachers': teachers,
    }
    return render(request, 'teachers/teacher_index.html', context)


# detail view
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


# create view
def addTeacherView(request):
    form = AddTeacherForm()
    if request.method == 'POST':
        form = AddTeacherForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            teacher_pin = form.cleaned_data['teacher_pin']
            designation = form.cleaned_data['designation']
            joined = form.cleaned_data['joined']
            phone = form.cleaned_data['phone']
            instance = Teacher(
                name=name, techer_id=teacher_pin,
                designation=designation, joined=joined,
                phone=phone
                )
            instance.save()
            form = AddTeacherForm()
            return redirect('/teachers/')

    else:
        form = AddTeacherForm()
    context = {
        'form': form,
    }
    return render(request, 'teachers/add_teacher.html', context)


# delete teacher
def deleteView(request, pk):
    obj = Teacher.objects.get(id=pk)
    obj.delete()
    return redirect('/teachers/')