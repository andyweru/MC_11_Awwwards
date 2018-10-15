from django.test import TestCase
from .models import *
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):
    def setUp(self):
        self.Pro= Editor(name = 'Wesh',)

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Pro,Editor))


class ProjectsTestClass(TestCase):

    def setUp(self):
        self.Pro= Projects(name = 'InstaClone', description='Test project')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Pro,Projects))

    def test_save_method(self):
        self.Pro.save_project()
        project = Projects.objects.all()
        self.assertTrue(len(project) > 0)

    def test_data(self):
        self.assertTrue(self.Pro.name,"test")

    def test_delete(self):
        post = Projects.objects.filter(id=1)
        post.delete()
        posts = Projects.objects.all()
        self.assertTrue(len(posts)==0)