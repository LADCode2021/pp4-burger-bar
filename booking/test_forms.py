from django.test import TestCase
from .forms import BookingForm, ContactForm, MyCustomLoginForm, MyCustomSignupForm, DateInput, DateOfBooking

# Create your tests here.


class TestBookingForm(TestCase):

    def test_id_is_required(self):
        form = BookingForm({'id': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('id', form.errors.keys())
        self.assertEqual(
            form.errors['id'][0], 'This field is required.'
            )
    
    def test_first_name_is_required(self):
        form = BookingForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(
            form.errors['first_name'][0], 'This field is required.'
            )
    

    def test_last_name_is_required(self):
        form = BookingForm({'last_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(
            form.errors['last_name'][0], 'This field is required.'
            )
    

    def test_phone_number_is_required(self):
        form = BookingForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.'
            )
    
    def test_email_address_is_required(self):
        form = BookingForm({'email_address': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email_address', form.errors.keys())
        self.assertEqual(
            form.errors['email_address'][0], 'This field is required.'
            )
    

    def test_email_address_is_required(self):
        form = BookingForm({'email_address': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email_address', form.errors.keys())
        self.assertEqual(
            form.errors['email_address'][0], 'This field is required.'
            )
    
    def test_date_of_booking_is_required(self):
        form = BookingForm({'date_of_booking': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date_of_booking', form.errors.keys())
        self.assertEqual(
            form.errors['date_of_booking'][0], 'This field is required.'
            )

    def test_time_of_booking_is_required(self):
        form = BookingForm({'time_of_booking': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time_of_booking', form.errors.keys())
        self.assertEqual(
            form.errors['time_of_booking'][0], 'This field is required.'
            )

    def test_number_of_people_is_required(self):
        form = BookingForm({'number_of_people': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('number_of_people', form.errors.keys())
        self.assertEqual(
            form.errors['number_of_people'][0], 'This field is required.'
            )
    

    def test_special_requests_is_not_required(self):
        form = BookingForm({'special_requests': ''})
        self.assertTrue(form.is_valid())
    

    def test_fields_are_explicit_in_form_metaclass(self):
        form = BookingForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'id',
                'first_name',
                'last_name',
                'email_address',
                'phone_number',
                'date_of_booking',
                'time_of_booking',
                'number_of_people',
                'special_requests'
            ]
            )

class TestContactForm(TestCase):

    def test_first_name_is_required(self):
        form = ContactForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(
            form.errors['first_name'][0], 'This field is required.'
            )
    
    def test_first_name_is_required(self):
        form = ContactForm({'last_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(
            form.errors['last_name'][0], 'This field is required.'
            )
    
    def test_email_address_is_required(self):
        form = ContactForm({'email_address': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email_address', form.errors.keys())
        self.assertEqual(
            form.errors['email_address'][0], 'This field is required.'
            )

    def test_phone_number_is_required(self):
        form = ContactForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.'
            )
    

    def test_comments_is_required(self):
        form = ContactForm({'comments': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('comments', form.errors.keys())
        self.assertEqual(
            form.errors['comments'][0], 'This field is required.'
            )