# coding: utf-8
import numpy as np
import json
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.measurement.models import Measurement
from django.contrib.auth import get_user_model
from django.db import models 
from .models import *
from . import pnn

User = get_user_model()

class CalcPnnAPI(APIView):

    def info(self, msg):
        logger = logging.getLogger("command")
        logger.info(msg)

    def normalization(self, beat_data):
        max_value = np.max(beat_data)
        min_value = np.min(beat_data)
        normalized_data = (beat_data - min_value)/(max_value - min_value)
        return normalized_data

    def post(self, request, format=json):
        print ("data=", request.data)
        time = request.data["time"]
        heart_beat = request.data["beat"]
        # TODO test実行時にapi clientからデータを受け取る際には、下記のスクリプトでrequestからデータを取得。
        #time = request.data.getlist("time")
        #heart_beat = request.data.getlist("beat")
        beat_data = [int(s) for s in heart_beat]
        time_data = [i for i in range(0, len(beat_data)*10, 10)]
        normalized_data = self.normalization(beat_data)
        peak_time, RRI, _ = pnn.find_RRI(time_data, normalized_data)

        pnn_time, pnn_data = pnn.cal_pnn(peak_time, RRI)
        
        user_obj = User.objects.get(
            dev_id = request.data["dev_id"]
        )
        measurement_obj = Measurement.objects.get(
            id = request.data["measurement_id"],
            user = user_obj
        )
        measurement_obj.end_time = time
        measurement_obj.save()

        beat_data = ",".join(map(str, beat_data))
        beat_data_obj = BeatData.objects.get(
            measurement = measurement_obj
        )
        pnn_data_obj = PnnData.objects.get(
             measurement = measurement_obj
        )
        
        if beat_data_obj.beat_data == "":
            beat_data_obj.beat_data = str(beat_data)
            beat_data_obj.save()
            pnn_data_obj.pnn_data = str(pnn_data) 
            # pnn_data_obj.pnn_time = str(pnn_time)
            pnn_data_obj.save()
        else:
            beat_data_obj.beat_data += "," + str(beat_data)
            beat_data_obj.save()
            pnn_data_obj.pnn_data += "," + str(pnn_data) 
            # pnn_data_obj.pnn_time += "," + str(pnn_time)
            pnn_data_obj.save()

        return Response(status=status.HTTP_201_CREATED)

