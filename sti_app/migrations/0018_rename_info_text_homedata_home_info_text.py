# Generated by Django 3.2.5 on 2022-06-30 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sti_app', '0017_auto_20220630_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homedata',
            old_name='info_text',
            new_name='home_info_text',
        ),
    ]