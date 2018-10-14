from django.shortcuts import render
from django.http  import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    projects = Project.display_projects()
    return render(request, "index.html", {"projects":projects[::-1]})

def search(request):
    return render(request, "search.html")


def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"project.html", {"project":project})
