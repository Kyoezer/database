# Generated by Django 4.1 on 2022-08-15 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_artist_profile_pubcountry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist_profile',
            name='pubdocument',
        ),
        migrations.AlterField(
            model_name='artist_profile',
            name='profile_type',
            field=models.CharField(blank=True, choices=[('select', 'Select'), ('Personal', 'Personal'), ('Company', 'Company'), ('Orginization', 'Orginization'), ('Group', 'Group')], default='select', max_length=32),
        ),
        migrations.AlterField(
            model_name='artist_profile',
            name='pubemployment_status',
            field=models.CharField(choices=[('select', 'Select'), ('Employed', 'Employed'), ('Unemployed', 'Unemployed'), ('Student', 'Student'), ('Business', 'Business')], default='select', max_length=32),
        ),
        migrations.AlterField(
            model_name='artist_profile',
            name='pubmarital_status',
            field=models.CharField(choices=[('select', 'Select'), ('Single', 'Single'), ('Married', 'Married')], default='select', max_length=32),
        ),
        migrations.AlterField(
            model_name='artist_profile',
            name='pudDzongkhag',
            field=models.CharField(choices=[('select', 'Select'), ('Bumthang', 'Bumthang'), ('Chukha', 'Chukha'), ('Dagana', 'Dagana'), ('Gasa', 'Gasa'), ('Haa', 'Haa'), ('Lhuntse', 'Lhuntse'), ('Mongar', 'Mongar'), ('Paro', 'Paro'), ('Pemagatshel', 'Pemagatshel'), ('Punakha', 'Punakha'), ('Samdrup Jongkhar ', 'Samdrup Jongkhar '), ('Samtse', 'Samtse'), ('Sarpang', 'Sarpang'), ('Thimphu', 'Thimphu'), ('Trashigang', 'Trashigang'), ('Trashiyangtse', 'Trashiyangtse'), ('Trongsa', 'Trongsa'), ('Tsirang', 'Tsirang'), ('Wangdue Phodrang', 'Wangdue Phodrang'), ('Zhemgang', 'Zhemgang')], default='select', max_length=32),
        ),
    ]
