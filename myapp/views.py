from django.shortcuts import render
from django.http  import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    projects = Project.display_projects()
    return render(request, "index.html", {"projects":projects[::-1]})
