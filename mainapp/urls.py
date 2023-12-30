from django.urls import path
from .views import StudentListCreateView, StudentRUDView


urlpatterns = [
    path('student_list/', StudentListCreateView.as_view(), name="student_list"),
    path('student_rud/<int:pk>/', StudentRUDView.as_view(), name="student_rud"),
]
