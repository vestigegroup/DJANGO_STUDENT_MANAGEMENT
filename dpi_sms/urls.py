from django.contrib import admin
from django.urls import path, include
from mainapp.views import redirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #stands for homepage
    path('welcome/', include('mainapp.urls')),
    #regx will say for whom it's been made :p
    path('', redirectView),
    path('clubs/', include('clubs.urls')),
    path('teachers/', include('teachers.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
