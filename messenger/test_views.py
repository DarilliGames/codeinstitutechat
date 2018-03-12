from django.test import TestCase
from .views import *
from .models import Message
from django.contrib.auth.models import User

class MessageViewTests(TestCase):
    def test_index_template(self):
        response = self.client.get('/messenger/')
        self.assertTemplateUsed(response, "messenger/index.html")
        
    def test_inbox_template(self):
        response = self.client.get('/messenger/inbox/')
        self.assertTemplateUsed(response, "messenger/inbox.html")
        
    def test_sent_template(self):
        response = self.client.get('/messenger/sent/')
        self.assertTemplateUsed(response, "messenger/sent.html")
        
    def test_singlemail_doesnotexist(self):
        response = self.client.get('/messenger/mail/af1')
        self.assertEqual(response.status_code, 404)
        
    def test_view_message_that_exists(self):
        sender = User(username="sender")
        sender.save()

        recipient = User(username="receiver")
        recipient.save()

        message = Message(
            subject = "Test Subject",
            body = "Test Body",
            sender = sender,
            recipient = recipient)
        message.save()

        response = self.client.get('/messenger/mail/1')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, "messenger/mail.html")