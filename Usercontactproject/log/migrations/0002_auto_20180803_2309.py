# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-03 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='contact',
            field=models.CharField(max_length=12),
        ),
    ]