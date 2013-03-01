import pdb
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import *

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        User.objects.create_user(username='t@t.com', email='t@t.com', password='testests')

    def test_profile(self):
        response = self.client.get('/users/t%40t.com/')
        self.failUnlessEqual(response.status_code, 200)

    def test_profile_list(self):
        response = self.client.get('/users/')
        self.failUnlessEqual(response.status_code, 200)
        
class LoggedInTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        User.objects.create_user(username='t@t.com', email='t@t.com', password='testests')
        self.client.login(username='t@t.com', password='testests')

    def test_profile(self):
        response = self.client.get('/users/t%40t.com/')
        self.assertTrue('Techniques' in response.content)
        self.failUnlessEqual(response.status_code, 200)

    def test_profile_list(self):
        response = self.client.get('/users/')
        self.assertTrue('Techniques' in response.content)
        self.failUnlessEqual(response.status_code, 200)
        
    def test_own_profile(self):
        response = self.client.get('/users/t%40t.com/')
        self.failUnlessEqual(response.status_code, 200)
