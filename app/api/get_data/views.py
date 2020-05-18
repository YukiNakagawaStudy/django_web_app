from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.db import models
from django.contrib.auth import get_user_model
from api.measurement.models import Measurement
from api.calc_data.models import PnnData
from api.calc_data.serializers import PnnDataSerializer
import logging

User = get_user_model()

class GetPnnAPI(APIView):
    permission_classes = (AllowAny,)

    def info(self, msg):
        logger = logging.getLogger("command")
        logger.info(msg)

    def post(self, request, format=None):
        # TODO 認証機能実装後↓の方法でmeasurement_obj取得する
        # measurement_obj = request.user.measurement_set.all().order_by("-id").first()
        user_obj = User.objects.get(id = request.data["user_id"])
        measurement_obj = Measurement.objects.filter(user = user_obj).order_by("-id").first()
        # measurement_obj = Measurement.objects.get(
        #     id = request.data["measurement_id"],
        #     #user = request.user
        # )
        print(measurement_obj)
        pnn_data_obj = PnnData.objects.get(
            measurement = measurement_obj,
            # id__gt = request.data["request_index"]
        )
        print(pnn_data_obj)
        serializer = PnnDataSerializer(pnn_data_obj)
        # print (serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
