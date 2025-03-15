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


class WatchListTestCase(APITestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='awais',password='awais1234')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream= models.StreamPlatform.objects.create(name="netflix",
            about="#1 stream platform",
            link="https://netflix.com")
        
        self.watch=models.WatchList.objects.create(
            platform = self.stream,
            title="X-MAN SEASON 1",
            storyline="A story of X man",
            genre="action",
            published=True,
            year=200

        )
        
    def test_watch_create(self):

        data = {

            "platform":self.stream,
            "title":"X-MAN SEASON 1",
            "storyline":"A story of X man",
            "genre":"action",
            "published":True,
            "year":200
        }

        response=self.client.post(reverse("watchlist"),data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_watch_list(self):
        response= self.client.get(reverse("watchlist"))
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_watch_ind(self):
        response= self.client.get(reverse("moviedetails" , args=(self.watch.id,)))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.get().title ,"X-MAN SEASON 1")



class ReviewTestCase(APITestCase):


    def setUp(self):
        self.user=User.objects.create_user(username='awais',password='awais1234')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream= models.StreamPlatform.objects.create(name="netflix",
            about="#1 stream platform",
            link="https://netflix.com")
        
        self.watch=models.WatchList.objects.create(
            platform = self.stream,
            title="X-MAN SEASON 1",
            storyline="A story of X man",
            genre="action",
            published=True,
            year=200

        )

        self.watch2=models.WatchList.objects.create(
            platform = self.stream,
            title="X-MAN ",
            storyline="A story of X man",
            genre="action",
            published=True,
            year=200

        )

        self.review=models.Reviews.objects.create(review_user=self.user, rating=5,comment='Was Good Movie', watchlist=self.watch2 , active=False)
        
    def test_review_create(self):
        data={

            "review_user":self.user,
            "rating":4,
            "comment":"Good Movie",
            "watchlist":self.watch,
            "active":True

        }

        responce=self.client.post(reverse("review_create", args=(self.watch.id,)) , data)
        self.assertEqual(responce.status_code , status.HTTP_201_CREATED)

    def test_review_create_unauth(self):

        data={

            "review_user":self.user,
            "rating":4,
            "comment":"Good Movie",
            "watchlist":self.watch,
            "active":True

        }

        self.client.force_authenticate(user=None)
        responce=self.client.post(reverse("review_create", args=(self.watch.id,)) , data)
        self.assertEqual(responce.status_code , status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):

        data={

            "review_user":self.user,
            "rating":5,
            "comment":"Good Movie - Updated",
            "watchlist":self.watch,
            "active":True

        }

        responce=self.client.put(reverse("review_detail" , args=(self.review.id,)), data )
        self.assertEqual(responce.status_code , status.HTTP_200_OK)








        
        







    
