from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length =60)
    post = HTMLField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(upload_to = 'images/', blank=True)


    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def display_projects(cls):
        projects=cls.objects.all()
        return projects

    @classmethod
    def find_project(cls, search_term):
        projects=cls.objects.filter(title__icontains=search_term)
        return projects


class Comment(models.Model):
    comment = models.CharField(max_length =80,null=True)
    user = models.ForeignKey(User,null=True)
    post = models.ForeignKey(Project,related_name='comments',null=True)

    def __str__(self):
        return self.comment