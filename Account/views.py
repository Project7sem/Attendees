from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.

def Home(request):
    return render(request, "Account/index.html")



def Registration(request):
    if request.method == 'POST':
        pass
        
    else:
        return render(request,"Account/registeration.html",{"regform":form})



def Login(request):
    return render(request, "Account/login.html")