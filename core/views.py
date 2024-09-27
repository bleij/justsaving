from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from task.models import Task
from task.forms import NewTaskForm


@login_required
def home(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    else:
        form = NewTaskForm()

    context = {'form': form}
    return render(request, 'core/index.html', context)


@login_required
def task_list(request):
    # tasks = Task.objects.filter(user=request.user).order_by("-id")
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task/tasks.html', context)
