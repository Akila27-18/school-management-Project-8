from django.contrib import admin
from .models import User, ClassRoom, Course, StudentProfile, ParentProfile, Exam, Mark, Attendance

admin.site.register(User)
admin.site.register(ClassRoom)
admin.site.register(Course)
admin.site.register(StudentProfile)
admin.site.register(ParentProfile)
admin.site.register(Exam)
admin.site.register(Mark)
admin.site.register(Attendance)
