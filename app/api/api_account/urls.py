from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', views.SignUpAPI.as_view(), name='sign-up'),
    path('signin/', views.SignInAPI.as_view(), name="sign-in"),
    path('signout/', views.SignOutAPI.as_view(), name='sign-out'),
]
