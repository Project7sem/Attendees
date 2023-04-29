from django.db import models
from Account.models import Teacher, Student, Courses, Semester, AdminUser, Faculty

# Create your models here.

class StudentEnrolled(models.Model):
    college_admin = models.OneToOneField(AdminUser, related_name="collegeadmin", on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name="studentenrolled")
    faculty = models.ForeignKey(Faculty, related_name ="facultyprovides",on_delete=models.CASCADE)


class TeacherEnrolled(models.Model):
    college_admin = models.OneToOneField(AdminUser, related_name="collegename", on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher, related_name="teacherenrolled")

class AssignCourse(models.Model):
    teacher = models.OneToOneField(Teacher, related_name="teaches_subject", on_delete=models.CASCADE)
    course = models.ManyToManyField(Courses, related_name="course_for")