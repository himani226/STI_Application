# Generated by Django 3.2.5 on 2022-06-28 06:48

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('sti_app', '0005_auto_20220628_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutdata',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now),
        ),
        migrations.AddField(
            model_name='footermenu',
            name='menu_link',
            field=models.CharField(default='#', max_length=200),
        ),
        migrations.AddField(
            model_name='headermenu',
            name='menu_link',
            field=models.CharField(default='#', max_length=200),
        ),
        migrations.AlterField(
            model_name='banner',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now),
        ),
        migrations.AlterField(
            model_name='footermenu',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now),
        ),
        migrations.AlterField(
            model_name='headermenu',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now),
        ),
        migrations.AlterField(
            model_name='homedata',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now),
        ),
    ]