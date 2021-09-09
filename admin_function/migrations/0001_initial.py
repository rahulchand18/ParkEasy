# Generated by Django 3.1.6 on 2021-02-23 07:07

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
            name='AnonymousParkingUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(default='vehicle', max_length=255)),
                ('person_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('vehicle_number', models.CharField(max_length=255)),
                ('related_admin_of_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]