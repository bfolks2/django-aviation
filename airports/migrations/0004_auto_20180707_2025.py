# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-07 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0003_auto_20180707_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runway',
            name='bearing',
            field=models.CharField(help_text='Bearing in degrees', max_length=13),
        ),
    ]
