from django.urls import path
from . import views

urlpatterns = [
    path("stdregister/",views.StudentRegistration,name="stdregister"),
    path("teacheregister/",views.TeacherRegistration, name="teacheregister"),
    path("clzregister/",views.InstituteRegistration,name="clzregister"),
    path("login/", views.Login, name='login'),
    path("logout/", views.Logout, name='logout'),
    path("profile/", views.Profile, name="profile"),
    path("dashboard/", views.Dashboard, name="dashboard"),
    path("othersprofile/<int:pk>",views.OthersProfile, name="othersprofile"),
    path("addcourse/",views.AddCourse,name="addcourse"),
    path("assign/", views.Assign,name="assign"),

]