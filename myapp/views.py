from django.http import HttpResponse
from .models import Project,task
from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateNewTask,CreateNewProject

# Create your views here.
def index(request):
    title = "titulo django con andres"
    return render(request, "index.html",{
        'titulo': title
    })

def about(request):
    username = "andres martinez"
    return render(request,'about.html',{
        'user': username
    })

def project(request):
    projects = Project.objects.all()
    return render(request,"projects/projects.html",{
        'projects': projects
    })

def tareas(request):
    tasks = task.objects.all()
    return render(request,"tasks/tasks.html",{
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'POST':
        form = CreateNewTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form = CreateNewTask()
        return render(request,'tasks/create_task.html',{
            'form' : form
        })
    
def create_project(request):
    if request.method == 'POST':
        form = CreateNewProject(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')
    else:
        form = CreateNewProject()
        return render(request,'projects/create_project.html',{
            'form' : form
        })
    
def project_detail(request,id):
    project = get_object_or_404(Project,id=id)
    tasks = task.objects.filter(project_id=id)
    return render(request,'projects/detail.html',{
        'project': project,
        'tasks': tasks
    })