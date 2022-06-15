from django.urls import reverse

from rest_framework.test import APITestCase


class RegisterTest(APITestCase):
    def test_register(self):
        data = {
            "username"      : "example",
            "email"         : "example@aaa.com",
            "password"      : "Password123!",
            "password_check": "Password123!"
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 201)