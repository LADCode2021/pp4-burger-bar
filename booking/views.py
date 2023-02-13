from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import BookingForm, ContactForm
from .models import Booking


def get_home(request):
    """
    Gets homepage and renders ContactForm.
    """

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
    """
    Gets bookings from Booking model for all bookings based
    on logged in users email address.
    """

    email = request.user.email
    bookings = Booking.objects.filter(email_address=email)
    context = {
        'email': email,
        'bookings': bookings
        }
    return render(request, 'booking/bookings.html', context)


def get_bookings_guest(request):
    """
    Gets booking made by guest user by matching id stored
    in session in make_booking against id posted to db.
    """

    id = request.session.get('id')
    bookings = Booking.objects.filter(id=id)
    context = {
        'id': id,
        'bookings': bookings
        }
    return render(request, 'booking/bookings_guest.html', context)


@login_required(login_url='accounts/login')
def get_manage_account(request):
    """
    Get manage_account page for logged in user.
    Or redirect to sign-in page and then load manage_account page.
    """

    return render(request, 'booking/manage_account.html')


@staff_member_required
def get_manage_bookings(request):
    """
    Get manage_bookings page if staff member is logged in.
    Or redirect to admin login page then get manage_bookings page.
    """

    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/manage_bookings.html', context)


def make_contact(request):
    """
    Get contact page and post ContactForm to db.
    """

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
    """
    Get thank_you page
    """

    return render(request, 'booking/contact_thank_you.html')


def make_booking(request):
    """
    Post BookingForm input to db. Store session id for use in
    guest_booking_guest. Redirect to get_bookings for logged in user.
    Redirect to get_booking_guest for guest user.
    """

    if request.method == 'POST':

        form = BookingForm(request.POST)
        if form.is_valid():
            request.session['id'] = request.POST['id']
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
    """
    Allow logged in user to edit their booking.
    Loads new page and renders with unique id to ensure
    only that booking can be edited.
    Redirect to login page if user logged out.
    """

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
def delete_booking(booking_id):
    """
    Allow logged in user to delete their booking.
    Loads new page and renders with unique id to ensure
    only that booking can be deleted.
    Redirect to login page if user logged out.
    """

    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('get_bookings')
