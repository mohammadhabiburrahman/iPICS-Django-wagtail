# Generated by Django 4.0.4 on 2022-05-31 07:08

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audioarticle',
            name='categoryName',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='stageName', chained_model_field='stageName', on_delete=django.db.models.deletion.CASCADE, to='home.categories', verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='audioarticle',
            name='parentTopicName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.audioarticle', verbose_name='Parent Topic Name'),
        ),
        migrations.AlterField(
            model_name='audioarticle',
            name='stageName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.stage', verbose_name='Stage Name'),
        ),
        migrations.AlterField(
            model_name='audioarticle',
            name='topicName',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Topic Name'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='categoryName',
            field=models.CharField(max_length=50, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='stageName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.stage', verbose_name='Stage Name'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='stageName',
            field=models.CharField(max_length=50, verbose_name='Stage Name'),
        ),
        migrations.AlterField(
            model_name='textualarticle',
            name='categoryName',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='stageName', chained_model_field='stageName', on_delete=django.db.models.deletion.CASCADE, to='home.categories', verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='textualarticle',
            name='learnMoreUrl',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='More URL'),
        ),
        migrations.AlterField(
            model_name='textualarticle',
            name='medlinePlusUrl',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Medline Plus URL'),
        ),
        migrations.AlterField(
            model_name='textualarticle',
            name='parentTopicName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.textualarticle', verbose_name='Parent Topic Name'),
        ),
        migrations.AlterField(
            model_name='textualarticle',
            name='stageName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.stage', verbose_name='Stage Name'),
        ),
        migrations.AlterField(
            model_name='textualarticle',
            name='topicName',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Topic Name'),
        ),
        migrations.AlterField(
            model_name='videoarticle',
            name='categoryName',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='stageName', chained_model_field='stageName', on_delete=django.db.models.deletion.CASCADE, to='home.categories', verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='videoarticle',
            name='parentTopicName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.videoarticle', verbose_name='Parent Topic Name'),
        ),
        migrations.AlterField(
            model_name='videoarticle',
            name='stageName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.stage', verbose_name='Stage Name'),
        ),
        migrations.AlterField(
            model_name='videoarticle',
            name='topicName',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Topic Name'),
        ),
    ]