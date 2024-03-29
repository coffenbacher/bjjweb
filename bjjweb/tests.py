import pdb
from django.conf import settings
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import *
from django.contrib.sites.models import Site
from urllib2 import urlopen

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        User.objects.create_user(username='t@t.com', email='t@t.com', password='testests')

    def test_home(self):
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)
    
    def test_css(self):
        if 'StaticFilesStorage' in settings.STATICFILES_STORAGE:
            assert self.client.get(settings.STATIC_URL + 'css/styles.css')
        else:
            assert urlopen(settings.STATIC_URL + 'css/styles.css')

    def test_register_GET(self):
        response = self.client.get('/accounts/register/')
        self.failUnlessEqual(response.status_code, 200)
    
    def test_register_POST(self):
        response = self.client.post('/accounts/register/', {
                                            'username': 'test@test.com',
                                            'email': 'test@test.com',
                                            'password1': 'testests',
                                            'password2': 'testests'})
        self.assertTrue(User.objects.get(email='test@test.com'))
        self.failUnlessEqual(response.status_code, 302)
        
    def test_login(self):
        response = self.client.get('/accounts/login/')
        self.failUnlessEqual(response.status_code, 200)
    
    def test_login_POST(self):
        response = self.client.post('/accounts/login', {'username': 'test@test.com', 'password': 'testests'})
        self.failUnlessEqual(response.status_code, 301)
    
    def test_profile(self):
        response = self.client.get('/users/t%40t.com/')
        self.failUnlessEqual(response.status_code, 200)
        
    def test_about(self):
        response = self.client.get('/about/')
        self.failUnlessEqual(response.status_code, 200)
    
class LoggedInTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        User.objects.create_user(username='t@t.com', email='t@t.com', password='testests')
        self.client.login(username='t@t.com', password='testests')
    
    def test_home_logged_in(self):
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 302)

    def test_about_logged_in(self):
        response = self.client.get('/about/')
        self.assertTrue('Techniques' in response.content)
        self.failUnlessEqual(response.status_code, 200)
