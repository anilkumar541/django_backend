from django.db import models

# models.py

from django.db import models

class Student(models.Model):
    # Fields for the Student model
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Additional fields can be added based on your requirements

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
