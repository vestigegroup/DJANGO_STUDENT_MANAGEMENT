from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #stands for homepage
    path('welcome/', include('mainapp.urls')),
    #regx will say for whom it's been made :p
    path('clubs/', include('clubs.urls')),
    path('teachers/', include('teachers.urls')),
]
