from django.contrib.auth import get_user_model
import csv

from bookings.models import Booking

CustomUser = get_user_model()


def run():
    with open('res_data.csv') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            # number = row['number']
            # arrival = row['arrival']
            # departure = row['departure']
            # no_of_people = row['no_of_people']
            # status = row['status']
            username = row['name']
            phone = row['phone']
            email = row['email']

    new_CustomUser = CustomUser(username=username, phone=phone, email=email)
    new_CustomUser.save()

    # users = list(CustomUser.objects.all())

    # new_Booking = Booking(
    #     number=number,
    #     arrival=arrival,
    #     departure=departure,
    #     no_of_people=no_of_people,
    #     status=status
    #
    # )
    #
    # new_Booking.save()
