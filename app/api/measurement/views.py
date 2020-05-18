from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import models
from django.contrib.auth import get_user_model
from api.measurement.models import Measurement
from api.measurement.serializers import MeasurementSerializer
from api.calc_data.models import *
import logging

User = get_user_model()

class MeasurementStartAPI(APIView):
    def info(self, msg):
        logger = logging.getLogger("command")
        logger.info(msg)

    def post(self, request, format=None):
        print (request.data)
        user_obj = User.objects.get(dev_id = request.data["dev_id"])
        measurement_obj = Measurement.objects.create(
            user = user_obj,
            start_time = request.data["start_time"]
        )
        beat_obj = BeatData.objects.create(
            measurement = measurement_obj,
            beat_data = ""
        )
        pnn_data_obj = PnnData.objects.create(
            measurement = measurement_obj,
            pnn_data = ""
        )
        serializer = MeasurementSerializer(measurement_obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MeasurementEndAPI(APIView):
    def info(self, msg):
        logger = logging.getLogger("command")
        logger.info(msg)

    def post(self, request, format=None):
        user_obj = User.objects.get(dev_id = request.data["dev_id"])
        measurement_obj = Measurement.objects.get(
            id = request.data["measurement_id"],
            user = user_obj
        )
        measurement_obj.end_time = request.data["end_time"]
        measurement_obj.save()
        serializer = MeasurementSerializer(measurement_obj)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)