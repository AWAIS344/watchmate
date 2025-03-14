from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status

from watchlist_app.api import serializers
from watchlist_app import models


class StreamPlatformTestCase(APITestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='awais',password='awais1234')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream= models.StreamPlatform.objects.create(name="netflix",
            about="#1 stream platform",
            link="https://netflix.com")

    def test_stream_create(self):

        data={
            "name":"netflix",
            "about":"#1 stream platform",
            "link":"https://netflix.com"
        }

        response= self.client.post(reverse("streamplatform-list") , data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_stream_list(self):
        response= self.client.get(reverse("streamplatform-list"))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_stream_ind(self):
        response= self.client.get(reverse("streamplatform-detail" , args=(self.stream.id,)))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    
