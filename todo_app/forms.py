from django.forms import ModelForm
from .models import Skill
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SkillForm(ModelForm):
        class Meta:
            model = Skill
            fields = ['title', 'description', 'complete']