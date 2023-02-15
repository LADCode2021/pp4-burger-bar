import uuid
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinLengthValidator, EmailValidator


TIME_CHOICES = (
        ('12:00:00', '12pm'),
        ('12:15:00', '12:15pm'),
        ('12:30:00', '12:30pm'),
        ('12:45:00', '12:45pm'),
        ('13:00:00', '1pm'),
        ('13:15:00', '1:15pm'),
        ('13:30:00', '1:30pm'),
        ('13:45:00', '1:45pm'),
        ('14:00:00', '2pm'),
        ('14:15:00', '2:15pm'),
        ('14:30:00', '2:30pm'),
        ('14:45:00', '2:45pm'),
        ('15:00:00', '3pm'),
        ('15:15:00', '3:15pm'),
        ('15:30:00', '3:30pm'),
        ('15:45:00', '3:45pm'),
        ('16:00:00', '4pm'),
        ('16:15:00', '4:15pm'),
        ('16:30:00', '4:30pm'),
        ('16:45:00', '4:45pm'),
        ('17:00:00', '5pm'),
        ('17:15:00', '5:15pm'),
        ('17:30:00', '5:30pm'),
        ('17:45:00', '5:45pm'),
        ('18:00:00', '6pm'),
        ('18:15:00', '6:15pm'),
        ('18:30:00', '6:30pm'),
        ('18:45:00', '6:45pm'),
        ('19:00:00', '7pm'),
        ('19:15:00', '7:15pm'),
        ('19:30:00', '7:30pm'),
        ('19:45:00', '7:45pm'),
        ('20:00:00', '8pm'),
        ('20:15:00', '8:15pm'),
        ('20:30:00', '8:30pm'),
        ('20:45:00', '8:45pm'),
        ('21:00:00', '9pm'),
        ('21:15:00', '9:15pm'),
        ('21:30:00', '9:30pm'),
        ('21:45:00', '9:45pm'),
        ('22:00:00', '10pm'),
        ('22:15:00', '10:15pm'),
        ('22:30:00', '10:30pm'),
        ('22:45:00', '10:45pm'),
    )


class Booking(models.Model):
    """
    Class to define fields for BookingForm and Booking table in db
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
        )
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    email_address = models.EmailField(validators=[EmailValidator()])
    phone_number = models.CharField(
        validators=[
            MinLengthValidator(
                11, message="Please enter valid phone number starting with 0"
                )
                ], max_length=11, null=False, blank=False
        )
    date_of_booking = models.DateField(default=timezone.now)
    time_of_booking = models.CharField(
        max_length=10, choices=TIME_CHOICES, default=""
        )
    number_of_people = models.IntegerField()
    special_requests = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):  # code adapted from Models Part 2 FST walkthrough
        return self.first_name + " " + self.last_name + " | " \
             + str(self.date_of_booking) + " at " + str(self.time_of_booking)


class Contact(models.Model):
    """
    Class to define fields for ContactForm and Contact table in db
    """

    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    email_address = models.EmailField(validators=[EmailValidator()])
    phone_number = models.CharField(validators=[
        MinLengthValidator
        (
            11, message="Please enter valid phone number starting with 0"
            )
            ], max_length=11, null=False, blank=False
            )
    comments = models.TextField()

    def __str__(self):  # code adapted from Models Part 2 FST walk-through
        return self.first_name + " " + self.last_name + " | "
