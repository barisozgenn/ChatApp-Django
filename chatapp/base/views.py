from django.shortcuts import render
# Create your views here.

roomList = [
    {'id':1, 'name': 'room name 1'},
    {'id':2, 'name': 'room name 2'},
    {'id':3, 'name': 'room name 3'},
]

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
