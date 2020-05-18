# coding: utf-8
from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Measurement(models.Model):
	"""Measurement Table"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	start_time = models.DateTimeField(verbose_name="start_time")
	end_time = models.DateTimeField(verbose_name="end_time", null=True)
