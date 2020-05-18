from rest_framework import serializers
from .models import PnnData
from api.measurement.serializers import MeasurementSerializer

class PnnDataSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer()
    class Meta:
        model = PnnData
        fields = [
            'id',
            'measurement',
            # 'pnn_time',
            'pnn_data',
        ]
        