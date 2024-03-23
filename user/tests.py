from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from user.models import CustomUser


class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.valid_payload = {
            'email': 'test@example.com',
            'username': 'test_user',
            'password': 'testpassword',
        }
        self.invalid_payload = {
            'email': 'invalidemail',
            'username': '',
            'password': 'testpassword',
        }

    def test_user_registration_valid_payload(self):
        response = self.client.post(self.register_url, data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_registration_invalid_payload(self):
        response = self.client.post(self.register_url, data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserLoginTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse('login')
        self.user = CustomUser.objects.create_user(email='test@example.com', username='test_user', password='testpassword')

    def test_user_login_valid_credentials(self):
        response = self.client.post(self.login_url, data={'email': 'test@example.com', 'password': 'testpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_login_invalid_credentials(self):
        response = self.client.post(self.login_url, data={'email': 'test@example.com', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
