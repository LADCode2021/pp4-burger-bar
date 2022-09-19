from django.db import models


class Booking(models.Model):
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    email_address = models.EmailField(default="email@email.com")
    phone_number = models.IntegerField()
    date_of_booking = models.DateField()
    time_of_booking = models.TimeField()
    number_of_people = models.IntegerField()
    special_requests = models.CharField(max_length=200)

    def __str__(self):  # code adapted from Models Part 2 FST walkthrough
        return self.first_name + " " + self.last_name + " | " \
             + str(self.date_of_booking) + " at " + str(self.time_of_booking)
