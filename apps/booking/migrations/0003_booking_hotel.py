# Generated by Django 4.2.9 on 2024-04-22 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_room_review_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='hotel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='booking.hotel'),
            preserve_default=False,
        ),
    ]
