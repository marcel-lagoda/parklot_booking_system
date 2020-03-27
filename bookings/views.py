from django.contrib.auth import get_user_model
from django.views.generic import DetailView, ListView, UpdateView

from .models import Booking


CustomUser = get_user_model()


class HomePageView(ListView):
    model = CustomUser
    template_name = 'home.html'
    paginate_by = 25


class UpdateRezView(UpdateView):
    model = Booking
    fields = ['arrival', 'departure', 'status']
    template_name = 'update_rez.html'


class DetailRezView(DetailView):
    model = Booking
    template_name = 'booking.html'
    context_object_name = 'booking'
