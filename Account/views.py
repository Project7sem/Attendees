from django.shortcuts import render,redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def Home(request):
    return render(request, "Account/index.html")



def Registration(request):
    if request.method == 'POST':
        pass
        
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


    