# Generated by Django 5.1.2 on 2024-10-16 01:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_booking_menu_delete_menuitem_delete_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='guess_number',
        ),
        migrations.AddField(
            model_name='booking',
            name='guest_number',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
