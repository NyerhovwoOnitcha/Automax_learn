# Generated by Django 5.1 on 2024-09-02 23:33

import localflavor.us.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_location_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='state',
            field=localflavor.us.models.USStateField(default='NY', max_length=2),
        ),
        migrations.AddField(
            model_name='location',
            name='zipcode',
            field=localflavor.us.models.USZipCodeField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='location',
            name='address_1',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
