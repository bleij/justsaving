from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from task.models import Task
from task.forms import NewTaskForm
from django.views.generic import ListView, UpdateView, DeleteView
from task.filters import TaskFilter


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


class TaskListView(ListView):
    model = Task
    template_name = 'task/tasks.html'
    context_object_name = 'tasks'

    # ordering = ['-date_posted']
    # paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            tasks = Task.objects.all()
            context['task'] = tasks
            context['total_tasks'] = round(tasks.filter(status='done').count() / tasks.count() * 100, 1)
            context['filter'] = TaskFilter(self.request.GET, queryset=self.get_queryset())
        return context
