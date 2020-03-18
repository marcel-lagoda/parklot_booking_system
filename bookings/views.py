from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


from .models import Booking


CustomUser = get_user_model()


class HomePageView(ListView):
    model = Booking
    template_name = 'home.html'
    context_object_name = 'bookings'