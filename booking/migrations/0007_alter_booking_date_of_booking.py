# Generated by Django 3.2.15 on 2023-02-14 09:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20230214_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_of_booking',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 9, 29, 42, 398974, tzinfo=utc)),
        ),
    ]
