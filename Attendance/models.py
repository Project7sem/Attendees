from django.db import models
from Account.models import User,Semester

# Create your models here.

class AttendanceDetails(models.Model):
    user = models.ForeignKey(User, related_name="attendance_user", on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, related_name="attendes_sem", on_delete=models.CASCADE)
    taken_on = models.DateTimeField(auto_now_add=True)
    time_frame = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    status = models.CharField(default="Present", max_length=50)

    def __str__(self):
        return f"{ self.user } - { self.taken_on }"

