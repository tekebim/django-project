from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from todo.models import Task
from todo.forms import EditTaskForm

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
            return redirect('todo:index')

    return render(request, 'todo/index.html', {'tasks': tasks})

def edit(request, task_id):
    # task = get_object_or_404(Task, id=task_id)
    try:
        task = Task.objects.get(id=task_id)
        # if this is a POST request we need to process the form data
        if request.method == "POST":
            # create a form instance and populate it with data from the request:
            form = EditTaskForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                todo = form.save(commit=False)
                todo.save()
        else :
            form = EditTaskForm()
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'todo/edit.html', {'task': task, 'form': form})

def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    # Get todo id
    todo = Task.objects.get(id=int(task_id))
    # Delete todo
    todo.delete()
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
