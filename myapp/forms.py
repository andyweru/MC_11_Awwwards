from .models import *
from django import forms

#......
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['editor', 'pub_date', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'post']
        fields = ['comment']