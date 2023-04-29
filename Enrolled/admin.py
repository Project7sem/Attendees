from django.contrib import admin
from .models import StudentEnrolled, TeacherEnrolled

admin.site.register(StudentEnrolled)
admin.site.register(TeacherEnrolled)