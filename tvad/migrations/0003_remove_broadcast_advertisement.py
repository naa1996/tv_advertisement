# Generated by Django 4.0.3 on 2022-03-09 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvad', '0002_remove_advertisement_broadcast_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broadcast',
            name='advertisement',
        ),
    ]
