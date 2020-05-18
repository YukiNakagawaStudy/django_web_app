# coding: utf-8
from django.db import models
from django.utils import timezone
from api.measurement.models import Measurement


class BeatData(models.Model):
	measurement = models.OneToOneField(Measurement, on_delete=models.CASCADE)
	beat_data = models.TextField(verbose_name="beat_data")

class PnnData(models.Model):
	"""心拍数データ"""
	measurement = models.OneToOneField(Measurement, on_delete=models.CASCADE)
	# TODO Pnnの時間は現状は測定された心拍データのうち、一番最後に測定された値の時間を用いている。
	# pnn_time = models.TextField(verbose_name="pnn_time")
	pnn_data = models.TextField(verbose_name="pnn")
	


