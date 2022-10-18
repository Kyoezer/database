# Generated by Django 4.1 on 2022-08-15 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_artist_profile_profile_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authuser',
            name='country',
        ),
        migrations.RemoveField(
            model_name='authuser',
            name='skills',
        ),
        migrations.AlterField(
            model_name='authuser',
            name='Dzongkhag',
            field=models.CharField(choices=[('select', '---Select Dzongkhag---'), ('Bumthang', 'Bumthang'), ('Chukha', 'Chukha'), ('Dagana', 'Dagana'), ('Gasa', 'Gasa'), ('Haa', 'Haa'), ('Lhuntse', 'Lhuntse'), ('Mongar', 'Mongar'), ('Paro', 'Paro'), ('Pemagatshel', 'Pemagatshel'), ('Punakha', 'Punakha'), ('Samdrup Jongkhar ', 'Samdrup Jongkhar '), ('Samtse', 'Samtse'), ('Sarpang', 'Sarpang'), ('Thimphu', 'Thimphu'), ('Trashigang', 'Trashigang'), ('Trashiyangtse', 'Trashiyangtse'), ('Trongsa', 'Trongsa'), ('Tsirang', 'Tsirang'), ('Wangdue Phodrang', 'Wangdue Phodrang'), ('Zhemgang', 'Zhemgang')], default='select', max_length=32),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='employment_status',
            field=models.CharField(choices=[('select', '---Select Employment---'), ('Employed', 'Employed'), ('Unemployed', 'Unemployed'), ('Student', 'Student'), ('Business', 'Business')], default='select', max_length=32),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='marital_status',
            field=models.CharField(choices=[('select', '---Select Maritals---'), ('Single', 'Single'), ('Married', 'Married')], default='select', max_length=32),
        ),
    ]
