# Generated by Django 4.0.3 on 2022-04-05 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvad', '0007_advertisement_number_repetitions'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='cost',
            field=models.FloatField(blank=True, default=0, verbose_name='Стоимость'),
            preserve_default=False,
        ),
    ]