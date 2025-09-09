from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('details/', views.teachers_details, name='teachers_details'),
    path('details/<int:teacher_id>/', views.teachers_details, name='teachers_details'),
    path('list/', views.teacher_list, name='teacher_list'),
]