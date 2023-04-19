from django.shortcuts import render,redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import User,Teacher,Student,TeacherProfile, StudentProfile, Semester, Courses
from django.contrib.auth.hashers import make_password
from Posts.models import BlogPost
from Assignements.models import CreateAssignment
# Create your views here.

def Home(request):
    return render(request, "Account/homepage.html")



def StudentRegistration(request):
    context ={}
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get("username")
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        password = request.POST.get("password")
        confirm_password = request.POST.get("c_password")
        print(email,username)
        if password == confirm_password:
            password = make_password(password)
            reg_user = Student.objects.create(email=email,username=username,password=password)
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
            reg_user = Teacher.objects.create(email=email,username=username,password=password)
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
    posts = BlogPost.objects.filter(user=request.user).all()
    all_users = User.objects.all()
    if request.user.role == 'ADMIN':
        return render(request,"Account/admindash.html",{"all_users": all_users})
    elif request.user.role == 'TEACHER':
        t_prof=TeacherProfile.objects.get(teacher=request.user)
        context={
            'profile':t_prof,
            "all_users": all_users
        }
        
        return render(request,"Account/profile.html",context)
    else:
        profile = StudentProfile.objects.get(student=request.user)
        assignment = CreateAssignment.objects.filter(sems=profile.sem)
        sem = Semester.objects.get(id=profile.sem.id)
        courses = sem.courses.all()
        context={
            'profile':profile ,
            'posts': posts,
            'assignments': assignment,
            'courses': courses,
            "all_users": all_users,

        }
    
        return render(request,"Account/profile.html",context)

def OthersProfile(request,pk):
    all_users = User.objects.all()
    userprofile = User.objects.get(id=pk)
    posts = BlogPost.objects.filter(user=userprofile).all()
    context={
        "all_users": all_users,
        "userprofile": userprofile,
        'posts':posts,
        }
    if userprofile.role=='TEACHER':
        teacher_profile = TeacherProfile.objects.filter(teacher=userprofile).all()
        context['teacher_profile']=teacher_profile
        
    elif userprofile.role=="STUDENT":
        student_profile =StudentProfile.objects.filter(student=userprofile).all()
        print(student_profile)
        context['student_profile'] = student_profile
    return render(request,"Account/othersprofile.html",context)

def Dashboard(request):
    return render(request,"Account/dashboard.html")

def Courses(request):
    return render(request,"Account/courses.html")

def Camera(request):
    return render(request, 'attendance/takeattendance.html')

