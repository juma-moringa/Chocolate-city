# Generated by Django 3.2.5 on 2021-07-25 14:56

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhood', '0004_auto_20210725_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='hood_description',
            field=models.TextField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='hood_location',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='hood_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='hood_photo',
            field=cloudinary.models.CloudinaryField(default='image', max_length=255, verbose_name='image'),
        ),
    ]
