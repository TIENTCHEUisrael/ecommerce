from django.http import HttpResponse
from django.shortcuts import render, redirect
from Chat.models import Room, Message


# Create your views here.

def home(request):
    return render(request, 'chat/home.html')


def room(request, roomz):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=roomz)
    return render(request, 'chat/room.html', {
        'username': username,
        'room': roomz,
        'room_details': room_details
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect(room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect(room + '/?username=' + username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')
