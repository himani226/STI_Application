# Generated by Django 3.2.14 on 2022-09-01 06:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('sti_app', '0004_remove_indicatordefinition_indicator_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechnologyArea',
            fields=[
                ('technology_area_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('pub_date', models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='TechnologyAreaDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology_name', models.CharField(max_length=200)),
                ('inventor_detail', models.CharField(max_length=200)),
                ('institute', models.CharField(max_length=200)),
                ('technology_abstract', models.CharField(max_length=1000)),
                ('technology_status', models.CharField(max_length=200)),
                ('technology_transferred', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(blank=True, default=django.utils.datetime_safe.datetime.now)),
                ('technology_area_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sti_app.technologyarea')),
            ],
        ),
    ]