from django import forms
from .models import Booking

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