from rest_framework import serializers
from .models import User, StudentProfile, ParentProfile, Course, Exam, Mark, Attendance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role']

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = StudentProfile
        fields = ['id', 'user', 'classroom', 'roll_number']

class ParentSerializer(serializers.ModelSerializer):
    children = StudentSerializer(many=True)
    class Meta:
        model = ParentProfile
        fields = ['id', 'user', 'children']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
