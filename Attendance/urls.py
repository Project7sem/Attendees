from django.urls import path
from . import views

urlpatterns = [
    path("", views.take_attendance, name='attendance'),
    path("start/",views.start_attendance, name="start"),

]