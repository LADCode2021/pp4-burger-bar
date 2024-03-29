from django import forms
from django.forms import TextInput, EmailInput, NumberInput, TimeInput
from django.utils.timezone import now
from allauth.account.forms import LoginForm, SignupForm
from .models import Booking, Contact


class DateInput(forms.DateInput):
    """
    Sets date input and disables previous dates
    Datepicker used from:
    https://mrasimzahid.medium.com/how-to-implement-django-datepicker-calender-in-forms-date-field-9e23479b5db

    Disabling previous dates taken from:
    https://stackoverflow.com/questions/74227268/how-to-make-a-date-picker-that-does-not-select-previous-dates-in-django
    """
    input_type = 'date'

    def get_context(self, name, value, attrs):
        attrs.setdefault('min', now().strftime('%Y-%m-%d'))
        return super().get_context(name, value, attrs)


class DateOfBooking(forms.Form):
    """
    Date of Booking
    """
    date_of_booking = forms.DateField(widget=DateInput)


"""
Some widgets adapated from:
https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa
"""


class BookingForm(forms.ModelForm):
    """
    Class to give metadata to BookingForm fields
    """
    class Meta:
        """
        Meta class for Booking model
        """

        model = Booking
        fields = [
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
                'placeholder': 'Email Address'
                }),
            'phone_number': TextInput(attrs={
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
    """
    Class to give metadata to ContactForm fields
    """
    class Meta:
        """
        Meta class for Contact model
        """
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
                'placeholder': 'First Name'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Last Name'
                }),
            'email_address': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email Address'
                }),
            'phone_number': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Phone Number'
                }),
            'comments': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Comments'
                }),
        }


class MyCustomLoginForm(LoginForm):
    """
    Class to allow css overwrite of allauth default field styling
    """

    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': "form-control",
            })


class MyCustomSignupForm(SignupForm):
    """
    Class to allow css overwrite of allauth default field styling
    """

    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': "form-control",
            })
