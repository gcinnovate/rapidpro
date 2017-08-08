# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-26 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flows', '0097_interrupt_runs_for_archived_flows'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlowPathRecentMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_uuid', models.UUIDField(help_text='Which flow node they came from')),
                ('to_uuid', models.UUIDField(help_text='Which flow node they went to')),
                ('text', models.CharField(max_length=640)),
                ('created_on', models.DateTimeField(help_text='When the message arrived')),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recent_messages', to='flows.FlowRun')),
            ],
        ),
    ]
