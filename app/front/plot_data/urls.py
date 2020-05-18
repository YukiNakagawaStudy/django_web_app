from django.contrib import admin
from . import views
from django.urls import path
from front.plot_data.views import *

urlpatterns = [
    path('show/', user_show, name='user_show'),
]