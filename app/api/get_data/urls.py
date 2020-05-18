from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('pnn/', views.GetPnnAPI.as_view(), name='get-pnn'),
]
urlpatterns = format_suffix_patterns(urlpatterns)