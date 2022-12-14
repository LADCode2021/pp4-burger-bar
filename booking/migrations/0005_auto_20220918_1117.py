# Generated by Django 3.2.15 on 2022-09-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_booking_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_of_booking',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='number_of_people',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time_of_booking',
            field=models.TimeField(null=True),
        ),
    ]
