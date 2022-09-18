from django.test import TestCase
from .models import Booking

class TestModels(TestCase):

    def test_string_method_returns_name(self):
        booking = Booking.objects.create(
            first_name='Test',
            last_name='Test',
            email_address='test@test.com',
            phone_number=int('07554433072'),
            date_of_booking='2023-01-01',
            time_of_booking='06:35',
            number_of_people=int('5'),
            special_requests='test'
            )
        self.assertEqual(
            str('booking'), 'Test' + " " + 'Test' + " | " + '2023-01-01' + " at " + '06:35')