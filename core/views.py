from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import StudentProfile, Attendance, Mark

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Mark, Attendance, StudentProfile

@login_required
def dashboard(request):
    user = request.user

    context = {'user': user}

    # Student Dashboard
    if user.role == 'student':
        try:
            student_profile = user.student_profile
            marks = Mark.objects.filter(student=student_profile)
            attendance = Attendance.objects.filter(student=student_profile)
            context.update({
                'marks': marks,
                'attendance': attendance
            })
        except StudentProfile.DoesNotExist:
            context['message'] = "No student profile linked to this account."

    # Teacher Dashboard
    elif user.role == 'teacher':
        context['message'] = "Welcome Teacher! You can view or manage students."

    # Parent Dashboard
    elif user.role == 'parent':
        parent_profile = getattr(user, 'parent_profile', None)
        if parent_profile:
            children = parent_profile.children.all()
            context['children'] = children
        else:
            context['message'] = "No linked student accounts found."

    # Admin Dashboard
    elif user.role == 'admin':
        context['message'] = "Welcome Admin! Manage everything here."

    else:
        context['message'] = "Role not recognized."

    return render(request, 'core/dashboard.html', context)

def home(request):
    return render(request, 'core/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid credentials'})
    return render(request, 'core/login.html')



from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import StudentProfile, ClassRoom

User = get_user_model()

def add_student(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Create user with 'STUDENT' role
        user = User.objects.create_user(username=username, password=password, role=User.STUDENT)

        # Optionally assign to a class (if you have one)
        classroom = ClassRoom.objects.first()  # or use a select field
        StudentProfile.objects.create(user=user, classroom=classroom)

        messages.success(request, f"Student '{username}' added successfully!")
        return redirect("students_list")

    return render(request, "core/add_student.html")

@login_required
def students_list(request):
    students = StudentProfile.objects.all()
    return render(request, 'core/students_list.html', {'students': students})
