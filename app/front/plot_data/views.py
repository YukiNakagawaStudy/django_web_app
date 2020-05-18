from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin # authのみ制限する場合

# Create your views here.


class UserShow(LoginRequiredMixin, TemplateView):
    template_name = 'user/show.html.haml'
    
user_show = UserShow.as_view()
