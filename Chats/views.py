from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required
def inbox(request):
    user = request.user
    messages = Message.get_message(user = user)
    active_chat = None
    chats = None

    if messages:
        message = messages[0]
        active_chat = message["user"].username
        chats = Message.objects.filter(user = user, receiver = message["user"])
        chats.update(is_read = True)

        for message in messages:
            if message["user"].username == active_chat:
                message["unread"] = 0
        context = {
            "chats": chats,
            "active_chat": active_chat,
            "messages": messages,
        }

        return render(request, "chats/inbox.html", context)

