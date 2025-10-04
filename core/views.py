from rest_framework import viewsets
from .models import School, Teacher, Student
from .serializers import SchoolSerializer, TeacherSerializer, StudentSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all().prefetch_related("students")
    serializer_class = SchoolSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().prefetch_related("subjects")
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().select_related("school")
    serializer_class = StudentSerializer
