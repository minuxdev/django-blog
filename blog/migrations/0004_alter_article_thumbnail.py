# Generated by Django 4.2.9 on 2024-01-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(blank=True, max_length=500, null=True, upload_to=''),
        ),
    ]