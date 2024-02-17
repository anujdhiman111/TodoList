from django.shortcuts import render, redirect

from .models import Todo


def todo_list(request):
    tasks = Todo.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Todo.objects.create(title=title)
    return redirect('todo_list')

def delete_task(request, task_id):
    task = Todo.objects.get(pk=task_id)
    task.delete()
    return redirect('todo_list')

def complete_task(request, task_id):
    task = Todo.objects.get(pk=task_id)
    if task.completed:
        task.completed = False
    else:
        task.completed = True
    task.save()
    return redirect('todo_list')