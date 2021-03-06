# Generated by Django 3.2.5 on 2021-07-26 10:34

import cloudinary.models
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
            name='Neighbourhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hood_photo', cloudinary.models.CloudinaryField(default='image', max_length=255, verbose_name='image')),
                ('hood_name', models.CharField(max_length=60)),
                ('hood_location', models.CharField(max_length=60)),
                ('hood_description', models.TextField(blank=True, max_length=150)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField(default=0)),
                ('email', models.CharField(blank=True, max_length=30)),
                ('profile_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('neighbourhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myhood.neighbourhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, null=True)),
                ('post', models.TextField()),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood_post', to='myhood.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postowner', to='myhood.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('business_email', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('neighbourhood_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='myhood.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_owner', to='myhood.profile')),
            ],
        ),
    ]
