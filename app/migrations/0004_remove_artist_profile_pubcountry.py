# Generated by Django 4.1 on 2022-08-15 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_authuser_country_remove_authuser_skills_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist_profile',
            name='pubcountry',
        ),
    ]