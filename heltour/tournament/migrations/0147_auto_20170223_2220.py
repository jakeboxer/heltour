# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-23 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0146_league_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='description',
            field=models.CharField(blank=True, max_length=1023),
        ),
    ]
