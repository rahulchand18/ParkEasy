# Generated by Django 3.1.6 on 2021-02-27 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_places_place_overview_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='place_overview_file',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]