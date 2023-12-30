from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display= ["id", "first_name", "last_name", "date_of_birth", "email", "phone_number", "address", "created_at", "updated_at"]
