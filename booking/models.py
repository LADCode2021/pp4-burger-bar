from django.db import models

# Create your models here.

class Bookings(models.Model):
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    phone_number = models.BigIntegerField(max_length=11)
    date_of_booking = models.DateField()
    time_of_booking = models.TimeField()
    number_of_people = models.IntegerField()
    special_requests = models.CharField(max_length=200)


