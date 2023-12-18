# Generated by Django 5.0 on 2023-12-18 15:58

import django.core.validators
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_article_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])]),
        ),
    ]