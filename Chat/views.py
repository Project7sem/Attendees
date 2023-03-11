from django.shortcuts import render,redirect

# Create your views here.

def Chat(request):
    return render(request,"chat/chatpage.html")