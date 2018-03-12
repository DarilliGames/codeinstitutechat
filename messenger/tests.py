from django.test import TestCase
from .views import get_index, sent, inbox, write_mail
from django.core.urlresolvers import resolve


# # Create your tests here.

class indexTest(TestCase):
    def test_indexTest_page_resolves(self):
        check_page = resolve('/messenger/')
        self.assertEquals(check_page.func, get_index)

    def test_inboxTest_page_resolves(self):
        check_page = resolve('/messenger/inbox/')
        self.assertEquals(check_page.func, inbox)
        
    def test_sentTest_page_resolves(self):
        check_page = resolve('/messenger/sent/')
        self.assertEquals(check_page.func, sent)
        
    def test_compossTest_page_resolves(self):
        check_page = resolve('/messenger/write/')
        self.assertEquals(check_page.func, write_mail)

    def test_message_requires_id(self):
        response = self.client.get('/messenger/messagea')
        self.assertEqual(response.status_code, 404)