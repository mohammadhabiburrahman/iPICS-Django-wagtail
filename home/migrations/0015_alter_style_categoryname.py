# Generated by Django 4.0.4 on 2022-06-28 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_audioarticle_audio_alter_videoarticle_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='categoryName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='style', to='home.categories', verbose_name='Category Name'),
        ),
    ]
