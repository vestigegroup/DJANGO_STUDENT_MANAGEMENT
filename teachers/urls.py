from django.urls import path
from .import views


app_name = 'teachers'
urlpatterns = [
    path('', views.index, name='teachershome'),
    path('<int:teacher_id>/detail/', views.teacher_detail, name='teacher_detail'),
    path('add/', views.addTeacherView, name='add'),
    path('del/<int:pk>/', views.deleteView, name='delete'),
]
