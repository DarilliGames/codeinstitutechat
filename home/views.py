from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from messenger.models import Message

def get_index(request):
    unread = request.user.messages_received.filter(read=False)
    return render(request, "home/index.html", {"unread" : len(unread)})


@login_required(login_url='login')
def get_secret(request):
    return render(request, "home/secret.html")