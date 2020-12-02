from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Task

def index(request):
    # latest_tasks_list = Task.objects.order_by('-created_date')[:5]
    tasks = Task.objects.order_by('-created_date')[:5]
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)

def edit(request):
    return HttpResponse("Edit")
