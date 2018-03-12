from django.test import TestCase
from .models import Message

class MessageModel(TestCase):
    def test_str_works(self):
        message = Message()
        message.subject = "Test Subject"
        self.assertEquals("Test Subject", str(message))