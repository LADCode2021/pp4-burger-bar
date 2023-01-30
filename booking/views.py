from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm, ContactForm
from django.core import validators

# Create your views here.

def get_home(request):
    return render(request, 'booking/index.html')


def get_bookings(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/bookings.html', context)

def make_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print('form saved')
            return redirect(get_thank_you)

    form = ContactForm()
    context = {
        'form': form
        }
    return render(request, 'booking/contact.html', context)


def get_thank_you(request):
    return render(request, 'booking/contact_thank_you.html')


def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            print('form saved')
            return redirect(get_bookings)
        else:
            print('broken')
   
    form = BookingForm()
    context = {
        'form': form
        }
    return render(request, 'booking/make_booking.html', context)

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            print('form saved')
            return redirect(get_bookings)
    form = BookingForm(instance=booking)
    context = {
        'form': form
        }
    return render(request, 'booking/edit_booking.html', context)

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('get_bookings')


