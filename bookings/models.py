from django.contrib.auth import get_user_model
from django.db import models


class Booking(models.Model):
    NEW = 'NEW'
    CANCELLED = 'CANCELLED'

    STATUS_CHOICE = [
        (NEW, 'NEW'),
        (CANCELLED, 'CANCELLED'),
    ]

    number = models.PositiveIntegerField(unique=True)
    arrival = models.DateField()
    departure = models.DateField()
    no_of_people = models.PositiveSmallIntegerField(default=1)
    status = models.CharField(max_length=16, choices=STATUS_CHOICE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='users')
