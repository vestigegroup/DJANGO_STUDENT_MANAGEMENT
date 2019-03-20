from django.urls import path
from .import views


app_name = 'teachers'
urlpatterns = [
    path('', views.index, name='teachershome'),
]