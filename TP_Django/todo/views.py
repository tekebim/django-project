from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Task

def index(request):
    # Query all tasks
    tasks = Task.objects.all()
    # Query only the latest tasks
    # tasks = Task.objects.order_by('-created_date')[:5]

    # Checking if the request method is a POST
    if request.method == "POST":
        # Checking if there is a request to add a todo
        if "task-add" in request.POST:
            # Get the content
            content = request.POST["task-content"]
            # Init the todo
            todo = Task(content=content, is_done=False)
            # Save the todo
            todo.save()
            # Reload the page
            return redirect('/todo/')
        # Checking if there is a request to add a todo
        if "task-delete" in request.POST:
            # Get the content
            task_id = request.POST["task-id"]
            # Get todo id
            todo = Task.objects.get(id=int(task_id))
            # Delete todo
            todo.delete()
        # Checking if there is a request to add a todo
        if "task-done" in request.POST:
            # Get the content
            task_id = request.POST["task-id"]
            # Get todo id
            todo = Task.objects.get(id=int(task_id))
            # Update field : is_done
            todo.is_done = True
            # Save the todo
            todo.save()

    return render(request, 'todo/index.html', {'tasks': tasks})

def edit(request, task_id):
    # task = get_object_or_404(Task, id=task_id)
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'todo/edit.html', {'task': task})
