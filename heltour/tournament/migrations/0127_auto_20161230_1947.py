# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-30 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0126_alternate_last_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternatesearch',
            name='status',
            field=models.CharField(blank=True, choices=[('started', 'Started'), ('all_contacted', 'All alternates contacted'), ('completed', 'Completed')], max_length=31),
        ),
        migrations.AlterField(
            model_name='scheduledevent',
            name='type',
            field=models.CharField(choices=[('notify_mods_unscheduled', 'Notify mods of unscheduled games'), ('notify_mods_no_result', 'Notify mods of games without results'), ('start_round_transition', 'Start round transition'), ('notify_players_unscheduled', 'Notify players of unscheduled games'), ('notify_players_game_time', 'Notify players of their game time')], max_length=255),
        ),
    ]
