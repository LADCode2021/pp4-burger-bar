from django.shortcuts import render

# Create your views here.

def get_booking_form(request):
    return render(request, 'booking/booking_form.html')
