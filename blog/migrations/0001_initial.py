# Generated by Django 5.0 on 2023-12-12 22:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('total_post', models.IntegerField(verbose_name='total posts')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255, unique=True)),
                ('body', models.TextField()),
                ('posted', models.BooleanField(default=False)),
                ('slug', models.SlugField()),
                ('thumbnail', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='thumbnails/')),
                ('create_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField()),
                ('views', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
            ],
        ),
    ]