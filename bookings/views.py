from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView

from .models import Booking

CustomUser = get_user_model()


class HomePageView(ListView):
    model = CustomUser
    template_name = 'home.html'
    paginate_by = 25



