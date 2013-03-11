import pdb
import json
from models import *
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import *

class FlowTest(TestCase):
    fixtures = ['initial_data.json', 'test_flows.json', 'test_users.json', 'test_techniques.json']

    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        User.objects.create_user(username='t@t.com', email='t@t.com', password='testests')
        self.client.login(username='t@t.com', password='testests')
        
    def test_flow(self):
        response = self.client.get('/flow/')
        self.failUnlessEqual(response.status_code, 200)

    def test_flow_show(self):
        f = Flow.objects.all()[0]
        response = self.client.get('/flow/%s/' % f.id)
        self.failUnlessEqual(response.status_code, 200)

    def test_flow_render(self):
        f = Flow.objects.all()[0]
        p = Technique.objects.get(name='Test Armbar')
        response = self.client.get('/flow/%s/render/' % f.pk)
        j = json.loads(response.content)
        for l in j['links']:
            self.assertFalse(l['source'] == p.pk) 
        self.assertTrue(j)
        self.failUnlessEqual(response.status_code, 200)
    
    def test_flow_color(self):
        f = Flow.objects.all()[0]
        response = self.client.get('/flow/%s/render/' % f.pk)
        self.assertTrue('color' in response.content)

    def test_flow_links(self):
        f = Flow.objects.all()[0]
        p = Technique.objects.get(name='Test Armbar')
        response = self.client.get('/flow/%s/render/' % f.pk)
        j = json.loads(response.content)
        self.assertTrue('links' in j)
        self.assertTrue(len(j['links']))
            
    def test_flow_create_GET(self):
        response = self.client.get('/flow/create/')
        self.failUnlessEqual(response.status_code, 200)
    
    def test_flow_create_POST(self):
        d = {'name': 'Test Flow POST',
            'positions': 1,
            'submissions': 1,
            'positional_improvements': 1,
            'positional_improvements': 2}
        response = self.client.post('/flow/create/', d)
        self.failUnlessEqual(response.status_code, 302)
        self.assertTrue(Flow.objects.get(name='Test Flow POST'))
    
    def test_flow_css(self):
        response = self.client.get('/static/css/force.css')
        self.failUnlessEqual(response.status_code, 200)
    
    def test_flow_js(self):
        response = self.client.get('/static/js/flow.js')
        self.failUnlessEqual(response.status_code, 200)
        response = self.client.get('/static/js/d3.v2.js')
        self.failUnlessEqual(response.status_code, 200)

    def test_flow_list_count(self):
        f = Flow.objects.all()[0]
        response = self.client.get('/flow/%s/render/' % f.pk)
        self.assertTrue(': %s' % f.techniques.count() in response.content)
        


