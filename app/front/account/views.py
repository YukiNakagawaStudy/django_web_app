from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as AuthLoginView
from django.views.generic import CreateView
from django.views.generic import TemplateView
from .form import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
import logging
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin # 全てのpermissionで制限する場合
from api.measurement.models import Measurement
from api.calc_data.models import PnnData
import json

class Signup(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name = 'user/signup.html.haml'
    def post(self, request, *args, **kwargs):
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # ここでログインさせる
            # login(request, user)
            # messages.info(request, form.cleaned_data.get('password'))
            return redirect(sign_in)
        else:
            return render(request, 'user/signup.html.haml', {'form': form})
    def get(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        return render(request, 'user/signup.html.haml', {"form": form})
sign_up = Signup.as_view()


class Signin(AuthLoginView):
    template_name = 'user/signin.html.haml'
    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data.get('username'), password = form.cleaned_data.get('password'))
            if not user:
                raise Exception("user not found.")
            measurement = user.measurement_set.all()
            print(measurement)
            pnn = list(PnnData.objects.filter(measurement__in = measurement).values_list('pnn_data', flat=True))
            print(pnn)
            return render(request, 'user/show.html.haml', {'user': user, 'pnn': pnn, 'user_id': user.id})
        else:
            return render(request, 'user/signin.html.haml', {"form": form})

sign_in=Signin.as_view()


