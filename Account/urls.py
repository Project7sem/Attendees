from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name='home'),
    path("stdregister/",views.StudentRegistration,name="stdregister"),
    path("clzregister/",views.InstituteRegistration,name="clzregister"),
    path("login/", views.Login, name='login'),
    path("logout/", views.Logout, name='logout'),
    path("profile/", views.Profile, name="profile"),
    path("dashboard/", views.Dashboard, name="dashboard"),

]