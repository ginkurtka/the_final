# Generated by Django 4.2.9 on 2024-04-24 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_booking_hotel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='hotel',
        ),
    ]
