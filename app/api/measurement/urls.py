from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('start/', views.MeasurementStartAPI.as_view(), name='measurement-start'),
    path('end/', views.MeasurementEndAPI.as_view(), name='measurement-end'),
]
urlpatterns = format_suffix_patterns(urlpatterns)