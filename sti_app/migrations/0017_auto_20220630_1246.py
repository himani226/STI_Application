# Generated by Django 3.2.5 on 2022-06-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sti_app', '0016_auto_20220629_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_image',
            field=models.ImageField(max_length=200, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='homedata',
            name='education_image',
            field=models.ImageField(max_length=200, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='homedata',
            name='info_image',
            field=models.ImageField(max_length=200, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='homedata',
            name='innovation_image',
            field=models.ImageField(max_length=200, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='homedata',
            name='mission_image',
            field=models.ImageField(max_length=200, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='homedata',
            name='plans_image',
            field=models.ImageField(max_length=200, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='homedata',
            name='policies_image',
            field=models.ImageField(max_length=200, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='homedata',
            name='research_image',
            field=models.ImageField(max_length=200, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='homedata',
            name='slider_image',
            field=models.ImageField(max_length=200, upload_to='media'),
        ),
    ]