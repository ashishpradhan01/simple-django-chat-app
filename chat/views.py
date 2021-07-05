from django.http.response import HttpResponse, HttpResponseServerError
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Room, Message
# Create your views here.

def index(request):
    return render(request, 'index.html')

def room(request, roomname):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=roomname)
    context={
        "roomname":roomname,
        "username":username,
        "room_details":room_details
    }
    return render(request, 'chat.html', context)

def checkroom(request):
    if(request.method == 'POST'):
        roomname = request.POST['roomid']
        username = request.POST['username']
        if(Room.objects.filter(name=roomname).exists()):
            return redirect("{}/?username={}".format(roomname, username))
        else:
            Room.objects.create(name=roomname).save()
            return redirect("{}/?username={}".format(roomname, username))


def sendmessage(request):
    uname=request.POST['username']
    roomname=request.POST['roomname']
    room_id = Room.objects.get(name=roomname)
    msg=request.POST['message']
    Message.objects.create(username=uname, room=room_id, message=msg).save()
    return HttpResponse("Message Sent Successfully")

def getmessage(request, room):
    room_name = Room.objects.get(name=room)
    all_messages = room_name.messages.all()
    # all_messages = Message.objects.filter(room=room_name.id)
    return JsonResponse({
        "messages":list(all_messages.values())
    })

def roomexist(request, room):
    isRoomExist = Room.objects.filter(name=room).exists()
    return JsonResponse({
            "isRoomExist": isRoomExist 
        })