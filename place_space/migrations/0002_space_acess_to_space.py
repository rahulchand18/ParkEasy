# Generated by Django 3.1.6 on 2021-02-25 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place_space', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='acess_to_space',
            field=models.IntegerField(default=0),
        ),
    ]
