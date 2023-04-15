from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Room, Message



class Index(LoginRequiredMixin, View):
    def get(self, request):
        chat_rooms = Room.objects.all()
        return render(request, "chat/chat.html",{'chat_rooms':chat_rooms})


class Roomview(LoginRequiredMixin, View):
    def get(self,request,room_name):
        room = Room.objects.filter(name=room_name).first()
        chats=[]
        if room:
            chats = Message.objects.filter(room=room).all()
            print(chats)
        else:
            room = Room(name=room_name)
            room.save()
        return render(request, "chat/chatpage.html", {"room_name":room_name,"chats":chats})



