from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm, ContactForm
from django.core import validators
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def get_home(request):

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
    return render(request, 'booking/index.html', context)

@login_required(login_url='accounts/login')
def get_bookings(request):
    email = request.user.email
    bookings = Booking.objects.filter(email_address=email)
    context = {
        'email': email,
        'bookings': bookings
        }
    return render(request, 'booking/bookings.html', context)


def get_bookings_guest(request):
    email = request.session.get('email_address')
    print(email)
    bookings = Booking.objects.filter(email_address=email)
    context = {
        'email': email,
        'bookings': bookings
        }
    return render(request, 'booking/bookings_guest.html', context)


def get_manage_account(request):

    return render(request, 'booking/manage_account.html')


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
            request.session['email_address'] = request.POST['email_address']
            form.save()
            print('form saved')
            if request.user.is_authenticated:
                return redirect(get_bookings)
            if not request.user.is_authenticated:
                return redirect(get_bookings_guest)

    form = BookingForm()
    context = {
        'form': form
        }
    return render(request, 'booking/make_booking.html', context)


@login_required(login_url='accounts/login')
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


@login_required(login_url='accounts/login')
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('get_bookings')

