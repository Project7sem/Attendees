from django.db import models
from Account.models import Faculty, Student, Semester, Courses, Teacher
# Create your models here.

class CreateAssignment(models.Model):
    assignment_name = models.CharField(max_length=500)
    descripton = models.TextField()
    assigned_by = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name="assignment_given")
    assigned_to = models.ManyToManyField(Student, related_name="assignment_recevied")
    subject = models.OneToOneField(Courses, on_delete=models.CASCADE)
    sems = models.ForeignKey(Semester,  on_delete=models.CASCADE)
    date_assigned = models.DateTimeField( auto_now_add=True)
    date_line = models.DateTimeField(auto_now=False, auto_now_add=False)


    def __str__(self):
        return self.assignment_name

class SubmitAssigment(models.Model):
    assignment = models.OneToOneField(CreateAssignment, related_name="assignment" ,on_delete=models.CASCADE)
    answer = models.FileField(upload_to="Assignemnt/", max_length=1000)
    submited_by = models.ForeignKey(Student, related_name="submited_by", on_delete=models.CASCADE)
    submited_to = models.OneToOneField(Teacher, related_name="submited_to", on_delete=models.CASCADE)
    submitted_on = models.DateTimeField( auto_now_add=True)

