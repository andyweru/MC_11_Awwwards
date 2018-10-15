from django.shortcuts import render
from django.http  import HttpResponse
from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm



# Create your views here.
def index(request):
    projects = Project.display_projects()
    return render(request, "index.html", {"projects":projects[::-1]})

def search(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.find_project(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"projects": searched_projects})
    else:
        message = "Project does not exist"
        return render(request, 'search.html',{"message":message})

    return render(request, "search.html")


def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"project.html", {"project":project})


@login_required(login_url='/accounts/login/')
def myprofile(request):
    current_user = request.user
    return render(request, "myprofile.html")


@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.editor = current_user
            project.save()
    else:
        form = NewProjectForm()
    return render(request, 'upload.html', {"form": form})