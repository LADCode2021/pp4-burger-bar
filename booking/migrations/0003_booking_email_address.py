# Generated by Django 3.2.15 on 2022-09-17 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_bookings_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='email_address',
            field=models.EmailField(default='email@email.com', max_length=254),
        ),
    ]