# Generated by Django 4.0.4 on 2022-06-20 14:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_categories_iconimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audioarticle',
            name='audio',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'flac', 'M4A', 'aac'])]),
        ),
        migrations.AlterField(
            model_name='videoarticle',
            name='video',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'MOV', 'avi', 'mkv', 'wmv', 'avi'])]),
        ),
    ]
