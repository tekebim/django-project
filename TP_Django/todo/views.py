from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from todo.models import Task
from todo.forms import EditTaskForm, AddTaskForm
from django.contrib import messages

def index(request):
    # Query all tasks
    tasks = Task.objects.all()
    # Query only the latest tasks
    # tasks = Task.objects.order_by('-created_date')[:5]

    # Checking if the request method is a POST
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
        else:
            messages.error(request, "Error")
    else :
        form = AddTaskForm()

    return render(request, 'todo/index.html', {'tasks': tasks, 'form': form})

def edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = EditTaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.cleaned_data
            todo = form.save(commit=False)
            todo.save()
    else :
        form = EditTaskForm(initial={'content': task.content, 'is_done': task.is_done})

    return render(request, 'todo/edit.html', {'task': task, 'form': form})

def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    # Get todo id
    todo = Task.objects.get(id=int(task_id))
    # Delete todo
    todo.delete()
    # Redirect to the index
    return redirect('todo:index')

def deleteAll(request):
    tasks = Task.objects.all()
    tasks.delete()
    # Redirect to the index
    return redirect('todo:index')

def deleteDone(request):
    tasks = Task.objects.filter(is_done=True)
    tasks.delete()
    # Redirect to the index
    return redirect('todo:index')

def finish(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    # Update field : is_done
    task.is_done = True
    # Save the todo
    task.save()
    # Redirect to the index
    return redirect('todo:index')
