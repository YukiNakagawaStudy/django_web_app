from django.contrib import admin
from . import views
from django.urls import path
from front.account.views import *


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('signin/', sign_in, name='sign_in'),
    path('signup/', sign_up, name='sign_up'),
]
