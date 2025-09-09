from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('', views.welcome_page, name='welcome'),
    path('bye/', views.bye_page, name='bye')
]