# Generated by Django 3.1.6 on 2021-02-23 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_space', models.BooleanField(default=False)),
                ('bike_space', models.BooleanField(default=False)),
                ('space_number', models.CharField(max_length=4)),
                ('occupied', models.BooleanField(default=False)),
                ('empty', models.BooleanField(default=True)),
                ('partial_occupied', models.BooleanField(default=False)),
                ('related_place', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='places.places')),
            ],
        ),
    ]
