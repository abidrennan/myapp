from django.test import TestCase
from django.urls import reverse
from todo_app.forms import SkillForm, CreateUserForm
from django.contrib.auth.models import User

class SkillFormTestCase(TestCase):

    def test_valid_form(self):
        data = {'title': 'title', 'description': 'description', 'complete': False}
        form = SkillForm(data=data)
        self.assertTrue(form.is_valid())

    def test_missing_title_invalid(self):
        # Test title field validation
        data = {'title': '', 'description': '', 'complete': ''}
        form = SkillForm(data=data)
        self.assertFalse(form.is_valid()) and self.assertIn('title', form.errors)