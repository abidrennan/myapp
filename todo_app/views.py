from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Skill
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
def home(request):
    return render(request, 'todo_app/home.html')

class SkillList(LoginRequiredMixin, ListView):
    model = Skill
    context_object_name = 'skill-list'

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        search_input = self.request.GET.get('search-area')
        if search_input:
            queryset = queryset.filter(title__icontains=search_input)
        return queryset
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skill-list'] = context['skill-list'].filter(user=self.request.user)
        context['count'] = context['skill-list'].filter(complete=False).count()

        context['search_input'] = self.request.GET.get('search-area', '')

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
        return reverse_lazy('home')
    
class SkillSignUp(FormView):
    template_name = 'todo_app/signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SkillSignUp, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(SkillSignUp, self).get(*args, **kwargs)