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

    # def save(self,*args, **kwargs):
    #     if self.user.ROLE=="TEACHER":
    #         assigned_by= self.user
    #         return super().save(*args, **kwargs)

    def __str__(self):
        return self.assignment_name
