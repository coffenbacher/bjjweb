import pdb
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import *
from models import *

class LoggedOutTest(TestCase):
    fixtures = ['initial_data.json', 'test.json']

    def setUp(self):
        self.client = Client()

    def test_list(self):
        response = self.client.get('/technique/')
        self.failUnlessEqual(response.status_code, 200)
    
    def test_create_GET(self):
        response = self.client.get('/technique/create/')
        self.failUnlessEqual(response.status_code, 302)

    def test_show(self):
        s = Technique.objects.all()[0]
        response = self.client.get('/technique/%s/' % s.pk)
        self.failUnlessEqual(response.status_code, 200)


class LoggedInTest(TestCase):
    fixtures = ['initial_data.json', 'test.json', 'test_users.json']

    def setUp(self):
        self.client = Client()
        self.client.login(username='test', password='test')
    
    def test_list(self):
        response = self.client.get('/technique/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertFalse('RelatedManager' in response.content)

    def test_create_youtube(self):
        t = Technique(name='test sub', type=TechniqueType.objects.all()[0], 
            level=Level.objects.all()[0], youtube_link='http://www.youtube.com/watch?v=lfiXMeyY15s',
            created_by=User.objects.all()[0])
        t.save()
        self.failUnlessEqual(t.youtube_id, 'lfiXMeyY15s')

    def test_create_GET(self):
        response = self.client.get('/technique/create/')
        self.assertTrue('Name' in response.content)
        self.assertTrue('Level' in response.content)
        self.assertTrue('Youtube' in response.content)
        self.failUnlessEqual(response.status_code, 200)
        
    def test_create_position_POST(self):
        d = {'type': 3, 'level': 1, 'name': 'Test Position', 'form-TOTAL_FORMS': 1, 'form-INITIAL_FORMS': 0, 'form-MAX_NUM_FORMS': '', 'form-0-image': '', 'form-0-id': ''}
        response = self.client.post('/technique/create/', d)
        self.failUnlessEqual(response.status_code, 302)
        self.assertTrue(Technique.objects.get(name='Test Position'))

    def test_edit_GET(self):
        s = Technique.objects.all()[0]
        response = self.client.get('/technique/%s/edit/' % s.pk)
        self.assertTrue(s.name in response.content)
        self.failUnlessEqual(response.status_code, 200)
    
    def test_edit_POST(self):
        s = Technique.objects.all()[0]
        self.assertTrue(s.level.pk == 1)

        d = {'type': 3, 'level': 2, 'name': 'Test Position2', 'form-TOTAL_FORMS': 1, 'form-INITIAL_FORMS': 0, 'form-MAX_NUM_FORMS': '', 'form-0-image': '', 'form-0-id': ''}
        
        response = self.client.post('/technique/%s/edit/' % s.pk, d)
        self.failUnlessEqual(response.status_code, 302)
        
        s = Technique.objects.all()[0]
        self.assertTrue(s.level.pk == 2)
