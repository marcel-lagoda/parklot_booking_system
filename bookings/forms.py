from django import forms
from django.forms import ModelForm

from .models import Booking


class UpdateRezForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['arrival', 'departure']
