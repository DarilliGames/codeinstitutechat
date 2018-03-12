from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', get_index, name="messages"),
    url(r'^inbox/', inbox, name="inbox"),
    url(r'^sent/', sent, name="sent"),
    url(r'^mail/(\d+)', get_mail, name="mail"),
    url(r'^write/', write_mail, name="write"),
    url(r'^send/', send, name="send"),
]