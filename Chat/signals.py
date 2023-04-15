from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Room
from Account.models import Courses

@receiver(post_save, sender=Courses)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Room.objects.create(name=instance)
