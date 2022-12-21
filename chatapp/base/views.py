from django.shortcuts import render
from .models import *
# Create your views here.

roomList = [
    {'id':1, 'name': 'room name 1'},
    {'id':2, 'name': 'room name 2'},
    {'id':3, 'name': 'room name 3'},
]

def users(request):
    users = UserModel.objects.all()
    context = {'users': users}
    return render(request, 'base/users.html', context )

def home(request):
    context = {'rooms': roomList}
    return render(request, 'base/home.html', context )

def rooms(request):
    return render(request, 'base/rooms.html')

def room(request, pk):
    room = None
    for item in roomList:
        if item['id'] == int(pk):
            room = item

    context = {'room': room}  

    return render(request, 'base/room.html', context)
