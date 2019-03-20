from django.urls import path
from .import views

app_name = 'clubs'
urlpatterns = [
    path('', views.clubshome, name='clubshome'),
    path('history/', views.clubs_history, name='history'),
]