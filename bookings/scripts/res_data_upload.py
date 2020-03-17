from django.contrib.auth import get_user_model
import csv

from bookings.models import Booking

CustomUser = get_user_model()


def run():
    """Upload csv data into separate models."""
    with open('res_data.csv') as csv_file:
        reader = csv.DictReader(csv_file)

        CustomUser.objects.all().delete()
        Booking.objects.all().delete()

        for row in reader:
            instance, _ = CustomUser.objects.get_or_create(
                name=row['name'],
                phone=row['phone'],
                email=row['email'],
            )

            created, _ = Booking.objects.get_or_create(
                number=row['number'],
                arrival=row['arrival'],
                departure=row['departure'],
                no_of_people=row['no_of_people'],
                status=row['status'],
                user=[instance][0]
            )
