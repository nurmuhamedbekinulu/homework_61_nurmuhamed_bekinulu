from webapp.models import Task
from webapp.forms import TaskForm
from django.views.generic import DeleteView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class TaskCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'task_create.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskDetail(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'task.html'
    model = Task


class TaskUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'task_update.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'task_confirm_delete.html'
    model = Task
    success_url = reverse_lazy('index')
