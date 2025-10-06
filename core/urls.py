from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-student/', views.add_student, name='add_student'),
    path('students/', views.students_list, name='students_list'),
]
