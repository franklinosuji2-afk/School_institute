from django.contrib import admin
from .models import Student

# Option 1: Simple registration
admin.site.register(Student)

# OR Option 2: If you want custom admin configuration, use this instead:
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['id']  # Add your actual field names here
#     search_fields = ['id']  # Add your actual field names here