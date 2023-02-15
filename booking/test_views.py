from django.test import TestCase
from django.contrib.auth.models import User
from .models import Booking, Contact

# Create your tests here.


class TestViews(TestCase):

    def setUp(self):
        user = User.objects.create_superuser(username='username', password='password')
        self.client.login(username='username', password='password')


    def test_get_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/index.html')


    def test_get_bookings_(self):
        response = self.client.get('/bookings')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/bookings.html')
    

    def test_get_bookings_guest_(self):
        response = self.client.get('/bookings_guest')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/bookings_guest.html')

    
    def test_get_manage_account_(self):
        response = self.client.get('/manage')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/manage_account.html')
    

    def test_get_admin_management_(self):
        response = self.client.get('/admin_management')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/admin_management.html')
    

    def test_get_manage_bookings_(self):
        response = self.client.get('/manage_bookings')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/manage_bookings.html')
    

    def test_get_manage_contacts_(self):
        response = self.client.get('/manage_contacts')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/manage_contacts.html')


    def test_can_make_contact_(self):
        response = self.client.post(
            '/contact', data={
                'first_name': 'test',
                'last_name': 'test',
                'phone_number': '07555555555',
                'email_address': 'test@test.com',
                'comments': 'test'
            }
            )
        self.assertRedirects(response, '/contact_thank_you')

    
    def test_can_delete_contact_(self):
        contact = Contact.objects.create(
            first_name='test',
            last_name='test',
            email_address='test@test.com',
            phone_number='07555555555',
            comments='test'
            )
        response = self.client.get(f'/delete_contact/{contact.id}')


    def test_get_thank_you_(self):
        response = self.client.get('/contact_thank_you')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/contact_thank_you.html')
    

    def test_can_make_booking_if_authenticated_(self):
        response = self.client.post(
            '/make', data={
                'id': 'c0a68fa4-c0fe-4b33-b37a-88bd1808e156',
                'first_name': 'test',
                'last_name': 'test',
                'email_address': 'test@test.com',
                'phone_number': '07555555555',
                'date_of_booking': '2023-02-20',
                'time_of_booking': '12:30:00',
                'number_of_people': '1',
                'special_requests': 'test'
            }
            )
        self.assertRedirects(response, '/bookings')

    
    def test_can_edit_booking_(self):
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
        response = self.client.get(f'/edit/{booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/edit_booking.html')

    

    def test_can_delete_booking_(self):
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
        response = self.client.get(f'/delete/{booking.id}')