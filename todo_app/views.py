from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Skill
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    return render(request, 'todo_app/index.html')

class SkillList(LoginRequiredMixin, ListView):
    model = Skill
    context_object_name = 'skills'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['count'] = context['skills'].filter(complete=False).count()
        return context

class SkillDetail(LoginRequiredMixin, DetailView):
    model = Skill
    context_object_name = 'skill'

class SkillCreate(LoginRequiredMixin, CreateView):
    model = Skill
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy("skill-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SkillCreate, self).form_valid(form)
    
class SkillUpdate(LoginRequiredMixin, UpdateView):
    model = Skill
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('skill-list')

class SkillDelete(LoginRequiredMixin, DeleteView):
    model = Skill
    context_object_name = 'skill'
    success_url = reverse_lazy('skill-list')
    template_name = 'todo_app/delete_skill.html'

class SkillLogin(LoginView):
    template_name = 'todo_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('skill-list')