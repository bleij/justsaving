from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, DeleteView
from .models import Task


@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.name = request.POST.get(f'task_{pk}')
    task.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
# class UpdateTask(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Task
#     fields = ['title', 'description']
#     template_name = 'core/index.html'
#     success_url = reverse_lazy('task_list')
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#
#     def test_func(self):
#         task = self.get_object()
#         return self.request.user == task.user


@login_required()
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
