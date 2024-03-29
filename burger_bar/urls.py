"""burger_bar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_home, name='home'),
    path('bookings', views.get_bookings, name='get_bookings'),
    path('bookings_guest', views.get_bookings_guest, name='get_bookings_guest'),
    path('contact', views.make_contact, name='contact'),
    path('contact_thank_you', views.get_thank_you, name='thank_you'),
    path('make', views.make_booking, name='make'),
    path('edit/<booking_id>', views.edit_booking, name='edit'),
    path('delete/<booking_id>', views.delete_booking, name='delete'),
    path('accounts/', include('allauth.urls')),
    path('manage', views.get_manage_account, name='manage'),
    path('manage_bookings', views.get_manage_bookings, name='manage_bookings'),
    path('manage_contacts', views.get_manage_contacts, name='manage_contacts'),
    path('delete_contact/<contact_id>', views.delete_contact, name='delete_contact'),
    path('admin_management', views.get_admin_management, name='admin_management'),
]
