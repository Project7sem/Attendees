from django.db import models
from Account.models import Teacher, Student, Courses, Semester

# Create your models here.
class TeacherEnrolled(models.Model):
    teacher = models.OneToOneField(Teacher, related_name ="teacher", on_delete=models.CASCADE)
    course = models.ManyToManyField(Courses, related_name="courses" )
    semester = models.ManyToManyField(Semester, related_name="semester")