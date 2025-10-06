from django.db import models
from django.contrib.auth.models import AbstractUser

# ==========================
# Custom User model
# ==========================
class User(AbstractUser):
    ADMIN = 'admin'
    TEACHER = 'teacher'
    STUDENT = 'student'
    PARENT = 'parent'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
        (PARENT, 'Parent'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=STUDENT)

    def __str__(self):
        return f"{self.username} ({self.role})"


# ==========================
# ClassRoom model
# ==========================
class ClassRoom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ==========================
# Course model
# ==========================
class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - {self.name}"


# ==========================
# StudentProfile
# ==========================
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# ==========================
# ParentProfile
# ==========================
class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent_profile')
    student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE, related_name='parent')

    def __str__(self):
        return self.user.username


# ==========================
# Exam
# ==========================
class Exam(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.course.name})"


# ==========================
# Mark
# ==========================
class Mark(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    max_marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.user.username} - {self.exam.name}"


# ==========================
# Attendance
# ==========================
class Attendance(models.Model):
    PRESENT = 'present'
    ABSENT = 'absent'
    STATUS_CHOICES = [
        (PRESENT, 'Present'),
        (ABSENT, 'Absent'),
    ]

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student.user.username} - {self.course.name} ({self.status})"
