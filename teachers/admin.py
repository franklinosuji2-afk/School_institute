from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'employee_id')
    search_fields = ("name", "employee_id", "subject")

# Register your models here.
