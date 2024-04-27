from django.test import TestCase
from django.contrib.auth.models import User
from todo_app.models import Skill

class ModelTestCase(TestCase):
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

    def test_skill_creation(self):
        self.assertEqual(self.skill.user, self.user)
        self.assertEqual(self.skill.description, "Test description")
        self.assertTrue(self.skill.complete)