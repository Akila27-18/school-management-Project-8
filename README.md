Django School/College Management System (minimal)
------------------------------------------------

Instructions:
1. Create a virtualenv and install dependencies:
   pip install django djangorestframework djangorestframework-simplejwt

2. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

3. Create a superuser:
   python manage.py createsuperuser

4. Run the development server:
   python manage.py runserver

API endpoints:
- /api/token/   -> obtain JWT (POST username & password)
- /api/token/refresh/ -> refresh token
- /api/parents/me/ -> parent profile (needs JWT)


from core.models import User, ClassRoom, StudentProfile, ParentProfile, Course, Exam, Mark, Attendance
import datetime

# --- CREATE USERS ---
admin = User.objects.create_user(username="admin", password="admin123", role="admin")
teacher1 = User.objects.create_user(username="mr_smith", password="teacher123", role="teacher")
teacher2 = User.objects.create_user(username="mrs_jones", password="teacher123", role="teacher")
parent1 = User.objects.create_user(username="parent_anna", password="parent123", role="parent")
parent2 = User.objects.create_user(username="parent_ben", password="parent123", role="parent")
student1 = User.objects.create_user(username="anna", password="student123", role="student")
student2 = User.objects.create_user(username="ben", password="student123", role="student")
student3 = User.objects.create_user(username="charlie", password="student123", role="student")

# --- CLASSROOMS ---
class_a = ClassRoom.objects.create(name="Class A")
class_b = ClassRoom.objects.create(name="Class B")

# --- STUDENT PROFILES ---
s1 = StudentProfile.objects.create(user=student1, classroom=class_a)
s2 = StudentProfile.objects.create(user=student2, classroom=class_a)
s3 = StudentProfile.objects.create(user=student3, classroom=class_b)

# --- PARENT PROFILES ---
ParentProfile.objects.create(user=parent1, student=s1)
ParentProfile.objects.create(user=parent2, student=s2)

# --- COURSES ---
math = Course.objects.create(code="MATH101", name="Mathematics", teacher=teacher1, classroom=class_a)
science = Course.objects.create(code="SCI101", name="Science", teacher=teacher2, classroom=class_a)
english = Course.objects.create(code="ENG101", name="English", teacher=teacher1, classroom=class_b)

# --- EXAMS ---
exam1 = Exam.objects.create(name="Mid Term", course=math, date=datetime.date.today())
exam2 = Exam.objects.create(name="Final Term", course=science, date=datetime.date.today())

# --- MARKS ---
Mark.objects.create(student=s1, exam=exam1, marks_obtained=85, max_marks=100)
Mark.objects.create(student=s2, exam=exam1, marks_obtained=90, max_marks=100)
Mark.objects.create(student=s1, exam=exam2, marks_obtained=80, max_marks=100)
Mark.objects.create(student=s2, exam=exam2, marks_obtained=70, max_marks=100)
Mark.objects.create(student=s3, exam=exam1, marks_obtained=75, max_marks=100)

# --- ATTENDANCE ---
today = datetime.date.today()
for s in [s1, s2, s3]:
    Attendance.objects.create(student=s, course=math, date=today, status=Attendance.PRESENT)
    Attendance.objects.create(student=s, course=science, date=today, status=Attendance.ABSENT)

print("✅ Sample data created successfully!")
