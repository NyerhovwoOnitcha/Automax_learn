# Generated by Django 5.1 on 2024-09-03 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Location',
            new_name='location',
        ),
    ]
