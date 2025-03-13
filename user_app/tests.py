from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
# Create your tests here.
class RegistrationTestCase(APITestCase):

    def test_register(self):
        data={
            "username":"test1",
            "email":"test@gmail.com",
            "password":"test123",
            "password2":"test123"
        }

        response = self.client.post( reverse("register") ,data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)