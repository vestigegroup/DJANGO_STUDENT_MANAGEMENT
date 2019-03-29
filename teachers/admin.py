from django.contrib import admin
from teachers.models import Teacher, TeacherInfo, TeacherQualification, EduLevel


admin.site.register(Teacher)
admin.site.register(TeacherInfo)
admin.site.register(TeacherQualification)
admin.site.register(EduLevel)