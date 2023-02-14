# Generated by Django 3.2.15 on 2023-02-14 09:19

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_booking_date_of_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_of_booking',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 9, 19, 6, 767833, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11, message='Please enter valid phone number')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11, message='Please enter valid phone number')]),
        ),
    ]
