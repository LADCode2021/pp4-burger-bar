# Generated by Django 3.2.15 on 2023-02-09 15:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_booking_date_of_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_of_booking',
            field=models.DateField(default=datetime.datetime(2023, 2, 9, 15, 15, 55, 870340, tzinfo=utc)),
        ),
    ]