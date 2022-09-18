from django.test import TestCase
from .models import Booking

# Create your tests here.


class TestViews(TestCase):

    def test_get_bookings(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/bookings.html')

    def test_get_make_booking_page(self):
        response = self.client.get('/make')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/make_booking.html')

    def test_get_edit_booking_page(self):
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
        response = self.client.get(f'/edit/{booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/edit_booking.html')

 # def test_can_make_booking(self):
        # data = [
            # {'first_name': 'Test'},
            # {'last_name': 'Test'},
            # {'email_address': 'test@test.com'},
            # {'phone_number': int('07554433072')},
            # {'date_of_booking': '2023-01-01'},
            # {'time_of_booking': '06:35'},
            # {'number_of_people': int('5')},
            # {'special_requests': 'test'}
        # ]
        # response = self.client.post('/make', data)
        # self.assertEqual(response, '/')

    def test_can_delete_booking(self):
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
        response = self.client.get(f'/delete/{booking.id}')
        self.assertRedirects(response, '/')
        existing_items = Booking.objects.filter(id=booking.id)
        self.assertEqual(len(existing_items), 0)
