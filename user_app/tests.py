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




class LoginLogoutTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='example',password="example12")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_Login(self):

        data={
            'username':"example",
            "password":"example12"
        }

        response=self.client.post(reverse('login'),data)

        # self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_logout(self):

        # self.token = Token.objects.get(user__username='example')
        self.client.force_authenticate(user=self.user)

        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response=self.client.post(reverse('logout'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)