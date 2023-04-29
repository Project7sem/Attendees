from django.shortcuts import render,redirect
from .forms import RegistrationForm, LoginForm, CourseForm
from django.contrib.auth import authenticate, login, logout
from .models import User,Teacher,Student,TeacherProfile, StudentProfile, Semester, Courses, Faculty
from django.contrib.auth.hashers import make_password
from Posts.models import BlogPost
from Assignements.models import CreateAssignment
from Enrolled.models import StudentEnrolled, TeacherEnrolled, AssignCourse
# Create your views here.




def StudentRegistration(request):
    context ={}
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get("username")
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        password = request.POST.get("password")
        confirm_password = request.POST.get("c_password")
        faculty = request.POST.get("faculty")
        print(email,username,faculty)
        if password == confirm_password:
            password = make_password(password)
            reg_user = Student.objects.create(email=email,username=username,password=password)
            reg_user.save()
            if reg_user:
                std_faculty = Faculty.objects.filter(name=faculty).first()
                std_enroll=StudentEnrolled.objects.create(college_admin=request.user, faculty= std_faculty)
                std_enroll.students.add(reg_user)
                std_enroll.save()
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
                teacher_enroll=TeacherEnrolled.objects.create(college_admin=request.user)
                teacher_enroll.teacher.add(reg_user)
                teacher_enroll.save()
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
        context={
            "adminUser": request.user,
            "posts": posts,
            "student_details": StudentEnrolled.objects.filter(college_admin=request.user).all(),
            "teacher_details": TeacherEnrolled.objects.filter(college_admin=request.user).all(),

        }
        return render(request,"Account/adminprofile.html",context)
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
    elif userprofile.role=="ADMIN":
        context['admin_profile'] = userprofile
    return render(request,"Account/othersprofile.html",context)

def Dashboard(request):
    return render(request,"Account/dashboard.html")



def AddCourse(request):
    faculties = Faculty.objects.all()
    context={
            "faculties" : faculties,
        }
    if request.user.role == 'ADMIN':
        if request.method=="POST":
            course = request.POST.get("coursename")
            faculty = request.POST.get("faculty")
            check_faculty = Faculty.objects.filter(name=faculty).first()
            add_course = Courses.objects.create(name=course,faculty=check_faculty)
            if add_course:
                add_course.save()
                context['message']= "Course added sucessfully"
                return render(request, "Account/addcourse.html",context )
            else:
                context['message']="Cannot create course"
                return render(request, "Account/addcourse.html",context )
        else:
            return render(request, "Account/addcourse.html",context)

def Assign(request):
    teachers_list = TeacherEnrolled.objects.filter(college_admin=request.user).all()
    course_list = Courses.objects.all()
    context={
            "teachers" : teachers_list,
            "courses" : course_list
        }
    if request.user.role == 'ADMIN':
        if request.method=="POST":
            form_course = request.POST.get("coursename")
            form_teacher = request.POST.get("teacher")
            assigning = AssignCourse.objects.create(teacher=form_teacher)
            if assigning:
                add_course.course.add(form_course)
                context['message']= "Course assigned successfull"
                return render(request, "Account/assigncourse.html",context )
            else:
                context['message']="Cannot assing  course"
                return render(request, "Account/assigncourse.html",context )
        else:
            return render(request, "Account/assigncourse.html",context)


