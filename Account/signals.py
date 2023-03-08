from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, Student, Teacher, TeacherProfile, StudentProfile, Institute, AdminProfile, AdminUser

@receiver(post_save, sender=Student)
def create_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(student=instance)


@receiver(post_save, sender=Teacher)
def create_profile(sender, instance, created, **kwargs):
    if created:
        TeacherProfile.objects.create(teacher=instance)


@receiver(post_save, sender=AdminUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        AdminProfile.objects.create(user=instance)

