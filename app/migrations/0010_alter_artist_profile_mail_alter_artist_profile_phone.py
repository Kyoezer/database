# Generated by Django 4.1 on 2022-08-17 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_artist_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist_profile',
            name='mail',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='artist_profile',
            name='phone',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
