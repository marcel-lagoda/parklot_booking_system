from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()

        user = User.objects.create_user(
            username='marcel',
            email='marcel@marcel.com',
            password='testpassword',
        )
        self.assertEqual(user.username, 'marcel')
        self.assertEqual(user.email, 'marcel@marcel.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
