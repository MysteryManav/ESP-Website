# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-26 19:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_remove_formstackappsettings_module'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formstackappsettings',
            options={'verbose_name_plural': 'Formstack app settings'},
        ),
    ]