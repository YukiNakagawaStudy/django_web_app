from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.CalcPnnAPI.as_view(), name='calc-data'),
]
urlpatterns = format_suffix_patterns(urlpatterns)