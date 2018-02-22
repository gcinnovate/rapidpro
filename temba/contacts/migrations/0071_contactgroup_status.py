# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-22 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0070_fix_mailto_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactgroup',
            name='status',
            field=models.CharField(choices=[('B', 'Initializing'), ('B', 'Building'), ('R', 'Ready')], default='B', max_length=1),
        ),
    ]
