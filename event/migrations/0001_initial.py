# Generated by Django 4.0.6 on 2022-07-13 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='addevent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=100, unique=True)),
                ('is_show_mail', models.BooleanField(default=True, verbose_name='show')),
                ('phone', models.CharField(blank=True, max_length=8, null=True, unique=True)),
                ('is_show', models.BooleanField(default=True, verbose_name='show')),
                ('owner', models.IntegerField(default=1)),
                ('title', models.CharField(max_length=100)),
                ('Dzongkhag', models.CharField(choices=[('select', '---select Dzongkhag---'), ('Bumthang', 'Bumthang'), ('Chukha', 'Chukha'), ('Dagana', 'Dagana'), ('Gasa', 'Gasa'), ('Haa', 'Haa'), ('Lhuntse', 'Lhuntse'), ('Mongar', 'Mongar'), ('Paro', 'Paro'), ('Pemagatshel', 'Pemagatshel'), ('Punakha', 'Punakha'), ('Samdrup Jongkhar ', 'Samdrup Jongkhar '), ('Samtse', 'Samtse'), ('Sarpang', 'Sarpang'), ('Thimphu', 'Thimphu'), ('Trashigang', 'Trashigang'), ('Trashiyangtse', 'Trashiyangtse'), ('Trongsa', 'Trongsa'), ('Tsirang', 'Tsirang'), ('Wangdue Phodrang', 'Wangdue Phodrang'), ('Zhemgang', 'Zhemgang')], default='select', max_length=32)),
                ('medium', models.CharField(choices=[('Dzongkha', 'Dzongkha'), ('English', 'English'), ('Sharchop', 'Sharchop'), ('Nepali', 'Nepali'), ('Other', 'Other')], default='Dzongkha', max_length=100)),
                ('image_event', models.ImageField(upload_to='event/')),
                ('discription', models.TextField(blank=True, max_length=300)),
                ('available', models.BooleanField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False, verbose_name='show')),
                ('profile', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.artist_profile')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]