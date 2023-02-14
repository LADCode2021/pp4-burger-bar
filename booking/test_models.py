from django.test import TestCase
from .models import Booking, Contact

class TestBookingModel(TestCase):

    def test_booking_string_method_returns_name(self):
        booking = Booking.objects.create(
            id='c0a68fa4-c0fe-4b33-b37a-88bd1808e156',
            first_name='test',
            last_name='test',
            email_address='test@test.com',
            phone_number='07555555555',
            date_of_booking='2023-02-20',
            time_of_booking='12:30:00',
            number_of_people='1',
            special_requests='test'
            )
        self.assertEqual(
            str(booking), 'test' + " " + 'test' + " | " + '2023-02-20' + " at " + '12:30:00')


class TestContactModel(TestCase):

    def test_contact_string_method_returns_name(self):
        contact = Contact.objects.create(
            first_name='test',
            last_name='test',
            email_address='test@test.com',
            phone_number='07555555555',
            comments='test'
            )
        self.assertEqual(
            str(contact), 'test' + " " + 'test' + " | ")
