# Generated by Django 4.1 on 2022-08-15 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_artist_profile_pubskills'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist_profile',
            name='pubcountry',
            field=models.CharField(choices=[('select', '---select Countries---'), ('Bhutan', 'Bhutan'), ('India', 'India'), ('USA', 'USA')], default='select', max_length=32),
        ),
    ]
