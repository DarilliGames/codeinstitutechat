from django.test import TestCase
from .views import get_index
from django.core.urlresolvers import resolve

# Create your tests here.

class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEquals(home_page.func, get_index)