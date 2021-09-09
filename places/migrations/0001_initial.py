# Generated by Django 3.1.6 on 2021-02-23 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
                ('total_space', models.IntegerField(default=10)),
                ('remaining_space', models.IntegerField(default=10)),
                ('occupied_space', models.IntegerField(default=0)),
                ('available_space', models.IntegerField(default=10)),
                ('number_of_bike_space', models.IntegerField(default=10)),
                ('number_of_car_space', models.IntegerField(default=10)),
                ('place_link', models.URLField(unique=True)),
                ('associate_admin', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='associated_place', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]