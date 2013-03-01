import pdb
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import *
from models import *

class LoggedOutTest(TestCase):
    fixtures = ['initial_data.json', 'test_techniques.json', 'test_users.json']

    def setUp(self):
        self.client = Client()

    def test_list(self):
        response = self.client.get('/technique/')
        self.failUnlessEqual(response.status_code, 200)
    
    def test_create_GET(self):
        response = self.client.get('/technique/create/')
        self.failUnlessEqual(response.status_code, 302)

    def test_show(self):
        s = Position.objects.all()[0]
        response = self.client.get('/technique/%s/' % s.uuid)
        self.failUnlessEqual(response.status_code, 200)


class LoggedInTest(TestCase):
    fixtures = ['initial_data.json', 'test_techniques.json', 'test_users.json']

    def setUp(self):
        self.client = Client()
        self.client.login(username='test', password='test')
    
    def test_list(self):
        response = self.client.get('/technique/')
        self.failUnlessEqual(response.status_code, 200)

    def test_create_GET(self):
        response = self.client.get('/technique/create/')
        self.assertTrue('Name' in response.content)
        self.assertTrue('Level' in response.content)
        self.assertTrue('Youtube' in response.content)
        self.failUnlessEqual(response.status_code, 200)
        
    def test_create_position_POST(self):
        d = {'tech-type': 'position', 'level': 1, 'name': 'Test Position',
            'media-image-content_type-object_id-TOTAL_FORMS': 3,
            'media-image-content_type-object_id-INITIAL_FORMS': 0,
            'media-image-content_type-object_id-MAX_NUM_FORMS': '',
            'media-image-content_type-object_id-0-id': '',
            'media-image-content_type-object_id-1-id': '',
            'media-image-content_type-object_id-2-id': '',
            }
        response = self.client.post('/technique/create/', d)
        self.failUnlessEqual(response.status_code, 302)
        self.assertTrue(Position.objects.get(name='Test Position'))


    def test_create_submission_POST(self):
        d = {'tech-type': 'submission', 'level': 1, 'name': 'Test Submission', 'start': 1,
            'media-image-content_type-object_id-TOTAL_FORMS': 3,
            'media-image-content_type-object_id-INITIAL_FORMS': 0,
            'media-image-content_type-object_id-MAX_NUM_FORMS': '',
            'media-image-content_type-object_id-0-id': '',
            'media-image-content_type-object_id-1-id': '',
            'media-image-content_type-object_id-2-id': '',
            }
        response = self.client.post('/technique/create/', d)
        self.failUnlessEqual(response.status_code, 302)
        self.assertTrue(Submission.objects.get(name='Test Submission'))
    
    def test_create_positional_improvement_POST(self):
        d = {'tech-type': 'p-improvement', 'level': 1, 'name': 'Test PositionalImprovement', 
            'type': 1,
            'description': '',
            'start': 1,
            'end': 1,
            'media-image-content_type-object_id-TOTAL_FORMS': 3,
            'media-image-content_type-object_id-INITIAL_FORMS': 0,
            'media-image-content_type-object_id-MAX_NUM_FORMS': '',
            'media-image-content_type-object_id-0-id': '',
            'media-image-content_type-object_id-1-id': '',
            'media-image-content_type-object_id-2-id': '',
            }
        response = self.client.post('/technique/create/', d)
        self.failUnlessEqual(response.status_code, 302)
        self.assertTrue(PositionalImprovement.objects.get(name='Test PositionalImprovement'))

    def test_edit(self):
        s = Position.objects.all()[0]
        response = self.client.get('/technique/%s/edit/' % s.uuid)
        self.failUnlessEqual(response.status_code, 200)
