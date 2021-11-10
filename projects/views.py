from django.shortcuts import render
from projects.models import Project

# Create your views here.

def project_index(request):
    projects = Project.objects.all()

    return render(request, 'projects/project_index.html', {
        'projects': projects
    })

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)

    return render(request, 'projects/project_detail.html', {
        'project': project
    })