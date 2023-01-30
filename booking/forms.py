from django import forms
from django.forms import TextInput, EmailInput, NumberInput, DateInput, TimeInput
from .models import Booking, Contact

"""
Datepicker used from:
https://mrasimzahid.medium.com/how-to-implement-django-datepicker-calender-in-forms-date-field-9e23479b5db
"""


class DateInput(forms.DateInput):
    input_type = 'date'


# Form class in forms.py
class DateofBooking(forms.Form):
    """
    Date of Booking
    """
    date_of_booking = forms.DateField(widget=DateInput)


"""
Some widgets adapated from:
https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa
"""

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'email_address',
            'phone_number',
            'date_of_booking',
            'time_of_booking',
            'number_of_people',
            'special_requests'
        ]
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
                }),
            'email_address': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email Addresss'
                }),
            'phone_number': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Phone Number'
                }),
            'date_of_booking': DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Date of Booking'
                }),
            'time_of_booking': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Time of Booking'
                }),
            'number_of_people': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Number of People'
                }),
            'special_requests': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Special Requests'
                }), 
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'email_address',
            'phone_number',
            'comments'
        ]
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
                }),
            'email_address': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email Addresss'
                }),
            'phone_number': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Phone Number'
                }),
            'comments': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Comments'
                }),
        }
