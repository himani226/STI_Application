# Generated by Django 3.2.14 on 2022-08-23 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sti_app', '0003_auto_20220805_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indicatordefinition',
            name='indicator_image',
        ),
    ]