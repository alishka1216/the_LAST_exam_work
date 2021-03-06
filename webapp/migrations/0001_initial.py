# Generated by Django 3.2.3 on 2021-05-29 06:06

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
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('update_ad', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя автора')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание')),
                ('data', models.DateField()),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор альбома')),
            ],
            options={
                'verbose_name': 'Альбомы',
                'verbose_name_plural': 'Альбом',
                'db_table': 'album',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('update_ad', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='подпись')),
                ('avatar', models.ImageField(upload_to='avatars', verbose_name='Картинка продукта')),
                ('status', models.CharField(choices=[('public', 'публичная'), ('private', 'приватная')], default='public', max_length=50, verbose_name='статус')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_photos', to='webapp.album', verbose_name='Альбом к фотографии')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
                'db_table': 'photo',
            },
        ),
    ]
