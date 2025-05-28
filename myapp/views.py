from django.http import HttpResponse
from .models import Project,task
from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateNewTask,CreateNewProject

#vista del index
def index(request):
    title = "titulo django con andres"
    return render(request, "index.html",{
        'titulo': title
    })

#vista del about
def about(request):
    username = "andres martinez"
    return render(request,'about.html',{
        'user': username
    })

# mostramos los proyectos que estan en la base de datos, en la tabla "Project"
def project(request):
    projects = Project.objects.all()
    return render(request,"projects/projects.html",{
        'projects': projects
    })

# mostramos los proyectos que estan en la base de datos, en la tabla "task"
def tareas(request):
    tasks = task.objects.all()
    return render(request,"tasks/tasks.html",{
        'tasks': tasks
    })

# mostramos el formulario para que el usuario escriba los proyectos
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

# mostramos el formulario para que el usuario escriba las tareas
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
    
# creamos una vista para poder ingresar a cada proyecto y ver detalladamente sus tareas
def project_detail(request,id):
    project = get_object_or_404(Project,id=id)
    tasks = task.objects.filter(project_id=id)
    return render(request,'projects/detail.html',{
        'project': project,
        'tasks': tasks
    })