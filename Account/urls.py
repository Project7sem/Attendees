from django.urls import path
from .views import Home, Contact, Registration, Login

urlpatterns = [
    path("", Home, name='home'),
    path("contact/", Contact, name="contact"),
    path("register/", Registration, name="register"),
    path("login/", Login, name='login'),

]