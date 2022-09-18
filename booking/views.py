from django.shortcuts import render, redirect
from .models import Booking

# Create your views here.


def get_bookings(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/bookings.html', context)


def make_booking(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_address = request.POST.get('email_address')
        phone_number = request.POST.get('phone_number')
        date_of_booking = request.POST.get('date_of_booking')
        time_of_booking = request.POST.get('time_of_booking')
        number_of_people = request.POST.get('number_of_people')
        special_requests = request.POST.get('special_requests')
        Booking.objects.create(
            first_name=first_name,
            last_name=last_name,
            email_address=email_address,
            phone_number=phone_number,
            date_of_booking=date_of_booking,
            time_of_booking=time_of_booking,
            number_of_people=number_of_people,
            special_requests=special_requests
            )

        return redirect(get_bookings)
    return render(request, 'booking/make_booking.html')
