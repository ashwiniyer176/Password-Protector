from django.urls.base import reverse
from accounts.models import CustomUser
from django.test import TestCase

# Create your tests here.


class AuthTests(TestCase):
    def makeNewUser(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secretpwd'
        }
        CustomUser.objects.create_user(**self.credentials)

    def test_login(self):
        """
        Test login for valid user
        """
        self.credentials = {
            'username': 'testuser',
            'password': 'secretpwd'
        }
        CustomUser.objects.create_user(**self.credentials)
        response = self.client.post(
            reverse('login'), self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_login_with_wrong_credentials(self):
        """
        Test login with invalid credentials
        """
        self.credentials = {
            'username': 'testuser2',
            'password': 'secretpw'
        }
        response = self.client.post(
            reverse('login'), self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
