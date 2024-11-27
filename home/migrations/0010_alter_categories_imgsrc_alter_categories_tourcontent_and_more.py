# Generated by Django 4.0.4 on 2022-06-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_categories_stagename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='imgSrc',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Img Src'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='tourContent',
            field=models.CharField(default='', max_length=200, verbose_name='Tour Content'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='tourKey',
            field=models.CharField(default='', max_length=200, verbose_name='Tour Key'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='tourContent',
            field=models.CharField(default='', max_length=200, verbose_name='Tour Content'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='tourKey',
            field=models.CharField(default='', max_length=200, verbose_name='Tour Key'),
        ),
    ]
