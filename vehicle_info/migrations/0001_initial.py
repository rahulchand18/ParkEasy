# Generated by Django 3.1.6 on 2021-02-23 07:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('place_space', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike_number', models.CharField(max_length=20)),
                ('bike_in', models.BooleanField(default=False)),
                ('booked_date_and_time', models.DateTimeField(default=datetime.datetime.now)),
                ('place', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='places.places')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=20)),
                ('car_in', models.BooleanField(default=False)),
                ('booked_date_and_time', models.DateTimeField(default=datetime.datetime.now)),
                ('place', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='places.places')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entering_time', models.DateTimeField()),
                ('leaving_time', models.DateTimeField()),
                ('related_car', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vehicle_info.car')),
                ('related_person', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='catime', to=settings.AUTH_USER_MODEL)),
                ('related_place', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='places.places')),
                ('related_space', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='place_space.space')),
            ],
        ),
        migrations.CreateModel(
            name='BikeTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entering_time', models.DateTimeField()),
                ('leaving_time', models.DateTimeField()),
                ('related_bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_info.bike')),
                ('related_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bitime', to=settings.AUTH_USER_MODEL)),
                ('related_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.places')),
                ('related_space', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='place_space.space')),
            ],
        ),
    ]
