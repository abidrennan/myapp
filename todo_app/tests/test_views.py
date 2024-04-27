from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from todo_app.models import Skill

class ViewsTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Create a Skill with complete=True
        self.skill = Skill.objects.create(
            user=self.user,
            description="Test description",
            complete=True,
            create=None
        )

    def test_home_view(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_app/home.html')

    def test_create_skill_view(self):
        client = Client()
        # assuming the URL pattern for creating a project is 'skill-create'
        response = client.get(reverse('skill-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_app/skill_form.html')
       
        # test POST request
        data = {'title': 'New Skill', 'description': 'New Description', 'complete': False}
        response = client.post(reverse('skill-create'), data=data)
        self.assertEqual(response.status_code, 302)

        # check if skill was created
        skill_count = Skill.objects.filter(user=self.user).count()
        self.assertEqual(skill_count, 2)

    def test_create_skill_view_invalid_form(self):
        client = Client()
        response = client.post(reverse('skill-create'), {})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required")


