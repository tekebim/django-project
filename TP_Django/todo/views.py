from django.shortcuts import render
from django.http import Http404
from django.template import loader
from .models import Task

def index(request):
    # latest_tasks_list = Task.objects.order_by('-created_date')[:5]
    tasks = Task.objects.order_by('-created_date')[:5]
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)

def edit(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'todo/edit.html', {'task': task})
