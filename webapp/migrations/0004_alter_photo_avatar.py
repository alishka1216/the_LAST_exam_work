# Generated by Django 3.2.3 on 2021-05-29 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_rename_name_album_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars', verbose_name='Картинка продукта'),
        ),
    ]
