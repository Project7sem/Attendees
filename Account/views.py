from django.shortcuts import render,redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import User,Teacher,Student
from django.contrib.auth.hashers import make_password

# Create your views here.

def Home(request):
    return render(request, "Account/index.html")



def StudentRegistration(request):
    context ={}
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("c_password")
        if password == confirm_password:
            password = make_password(password)
            reg_user = User.objects.create(email=email,username=username,password=password)
            reg_user.save()
            if reg_user:
                context['message'] = "User registred successfully"
                return redirect("login")
            else:
                context['message']="Cannot create user"
                return redirect('stdregister')

        else:
            context['message']="Password didn't matched try again"
            return render(request,"Account/student_register.html", context)
    else:
        return render(request,"Account/student_register.html")

def TeacherRegistration(request):
    context ={}
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("c_password")
        if password == confirm_password:
            password = make_password(password)
            reg_user = User.objects.create(email=email,username=username,password=password)
            reg_user.save()
            if reg_user:
                context['message'] = "User registred successfully"
                return redirect("login")
            else:
                context['message']="Cannot create user"
                return redirect('stdregister')

        else:
            context['message']="Password didn't matched try again"
            return render(request,"Account/teacher_register.html", context)
    else:
        return render(request,"Account/teacher_register.html")


def InstituteRegistration(request):
    context ={}
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get("institute")
        password = request.POST.get("password")
        confirm_password = request.POST.get("c_password")
        if password == confirm_password:
            password = make_password(password)
            reg_user = User.objects.create(email=email,username=username,password=password)
            if reg_user:
                context['message'] = "User regestred successfully"
                return redirect("login")
            else:
                context['message']="Cannot create user"
                return redirect('clzregister')

        else:
            context['message']="Password didn't matched try again"
            return render(request,"Account/registeration.html", context)
    else:
        return render(request,"Account/registeration.html")




def Login(request):
    context ={}
    if request.user.is_authenticated:
        return redirect("home")
    elif request.method == "POST":
        login_form =LoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            auth_user = authenticate(email=email, password=password)
            if auth_user:
                try:
                    login(request, auth_user)
                    return redirect("home")
                except Exception as e:
                    context['message']=e
                    return redirect("login")
            else:
                context['message'] = "user cannot be authenticated"
                return redirect("login")
        else:
            context['message'] = "User not found please login first and try again"
            return redirect("login")
    else:
        login_form = LoginForm()
        context['login_form'] = login_form
        return render(request, "Account/login.html", context)

def Logout(request):
    logout(request)
    return redirect("login")

def Profile(request):
    if request.user.role == 'ADMIN':
        return render(request,"Account/admindash.html")
    return render(request,"Account/profile.html")

def Dashboard(request):
    return render(request,"Account/dashboard.html")

