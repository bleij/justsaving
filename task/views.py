from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import NewTaskForm


@login_required
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    if task.user == request.user:
        if request.method == 'GET':
            form = NewTaskForm(instance=task)
            return render(request, template_name='task/task_edit.html', context={'task': task, 'form': form})
        elif request.method == 'POST':
            form = NewTaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('task_list')
    else:
        return redirect('task_list')


@login_required
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if task.user == request.user:
        task.delete()
    return redirect('task_list')


