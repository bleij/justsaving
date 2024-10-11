from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from task.models import Task
from task.forms import NewTaskForm
from task.filters import TaskFilter


@login_required
def create_task(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            if not request.user.groups.filter(name='Project Manager').exists():
                task.assigned_to = request.user
            task.save()
            return redirect('task_list')
    else:
        form = NewTaskForm()

    if not request.user.groups.filter(name='Project Manager').exists():
        form.fields['assigned_to'].disabled = True
        form.fields['assigned_to'].initial = request.user

    context = {'form': form}
    return render(request, 'core/create_task.html', context)


@login_required
def task_list_view(request):
    tasks = Task.objects.all()

    if request.GET.get('assigned_to_me'):
        tasks = tasks.filter(assigned_to=request.user)

    if request.user.is_authenticated:

        if tasks.exists():
            total_tasks = round(tasks.filter(status='done').count() / tasks.count() * 100, 1)
        else:
            total_tasks = 0

        task_filter = TaskFilter(request.GET, queryset=tasks)

        context = {
            'tasks': task_filter.qs,
            'total_tasks': total_tasks,
            'filter': task_filter,
        }

        return render(request, 'task/tasks.html', context)
