from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name='home'),
    path("stdregister/",views.StudentRegistration,name="stdregister"),
    path("teacheregister/",views.TeacherRegistration, name="teacheregister"),
    path("clzregister/",views.InstituteRegistration,name="clzregister"),
    path("login/", views.Login, name='login'),
    path("logout/", views.Logout, name='logout'),
    path("profile/", views.Profile, name="profile"),
    path("dashboard/", views.Dashboard, name="dashboard"),
    path("course/",views.Courses, name='course'),
    path("camera/",views.Camera, name='camera'),

]