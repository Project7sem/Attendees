from django.contrib import admin
from .models import User, Student, Teacher,StudentProfile, TeacherProfile, Institute, Courses, Faculty, Semester, AdminUser, AdminProfile
# Register your models here.
admin.site.register(User)
admin.site.register(Institute)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(TeacherProfile)
admin.site.register(Courses)
admin.site.register(Faculty)
admin.site.register(Semester)
admin.site.register(StudentProfile)
admin.site.register(AdminUser)
admin.site.register(AdminProfile)