# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msgs', '0090_auto_20170407_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='exportmessagestask',
            name='system_label',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
