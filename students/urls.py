from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('list/', views.student_list, name='list'),
    path('details/', views.student_details, name='student_details'),
    path('details/<int:student_id>/', views.student_details, name='student_details'),
   
]