from django import forms
from .models import task,Project

class CreateNewProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']

    name = forms.CharField(label='Nombre del proyecto:',max_length=200)

class CreateNewTask(forms.ModelForm):
    class Meta:
        model = task
        fields = ['title','description','project']

    title = forms.CharField(label='Titulo',max_length=200)
    description = forms.CharField(label='descripción',widget=forms.Textarea)
    project = forms.ModelChoiceField(
        queryset = Project.objects.all(),
        label = 'Proyectos:',
        empty_label = 'Elige el proyecto para tu tarea'
    )
    