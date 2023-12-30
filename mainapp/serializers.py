# serializers.py

from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'address', 'created_at', 'updated_at')
