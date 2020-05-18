from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Tests(APITestCase):
        
    def test_signup(self):
        print ("\n")
        print ("TEST_SIGN UP start")
        print ("-"*40)

        data = {
            "email": "abc@logbii.com", 
            "password": "A3B4C5TMed8", 
            "username": "Logbii",
            "first_name": "yuki",
            "last_name": "nakagawa"
        }
        
        url = reverse("sign-up")
        print ("URL = ", url)
        
        response = self.client.post(url, data)
        
        print ("COUNT = ", User.objects.count())
        
        print ("Response data : ", response.data)

    def test_signin(self):
        print ("\n")
        print ("TEST_LOGIN start")
        print ("-"*40)

        validated_data = {
            "username": "Logbii",
            "email": "abc@logbii.com", 
            "password": "A3B4C5TMed8",
            "first_name": "yuki",
            "last_name": "nakagawa"
        }
        
        User.objects.create_user(email=validated_data['email'],
                                 username=validated_data['username'],
                                 first_name=validated_data["first_name"],
                                 last_name=validated_data["last_name"], 
                                 password=validated_data['password'])
        
        data = {
            "username": "Logbii",
            "password": "A3B4C5TMed8"
        }
        
        url = reverse("sign-in")
        print ("URL = ", url)
        
        response = self.client.post(url, data)
        
        # print ("COUNT = ", User.objects.count())
        
        print ("Response data : ", response.data)
