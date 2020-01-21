# Generated by Django 2.0.7 on 2020-01-19 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScooterAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scooter_lati', models.FloatField()),
                ('scooter_long', models.FloatField()),
                ('scooter_status', models.CharField(choices=[('A', 'Available'), ('B', 'Booked'), ('I', 'InService')], max_length=15)),
            ],
        ),
    ]
