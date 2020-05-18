from django.core.management.base import BaseCommand, CommandError
from django.db import models
from django.contrib.auth import get_user_model
import matplotlib.pyplot as plt
import numpy as np
from api.measurement.models import Measurement
from api.calc_data.models import BeatData
from api.calc_data import pnn

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(id=1)
        measurement = Measurement.objects.get(id=18)

        # Beat data
        beats_data = BeatData.objects.get(measurement=measurement).beat_data
        temp_data = beats_data.split(",")
        beat_data = np.array([int(s) for s in temp_data])
        time_data = np.array([i for i in range(0, len(beat_data)*10, 10)])*0.001
        num = int(len(beat_data)/1000)
        for i in range(num):
            plt.plot(time_data[800+i*1000:1200+i*1000], beat_data[800+i*1000:1200+i*1000])
            plt.show()

        # for beat_data in beats_data:
        #     beat_data = beat_data.split(",")
        #     beat_data = [int(s) for s in beat_data]
        #     beat_data = np.array(beat_data)
        #     max_value = np.max(beat_data)
        #     min_value = np.min(beat_data)   
        #     normalized_data = (beat_data - min_value)/(max_value - min_value)
        #     time_data = [i for i in range(0, len(beat_data)*5, 5)]
        #     peak_time, _, peaks = pnn.find_RRI(time_data, normalized_data)
        #     time_data = np.array(time_data) * 0.001
        #     plt.plot(time_data, beat_data)
        #     plt.plot(peak_time, beat_data[peaks], "o",color="red")
        #     plt.show()