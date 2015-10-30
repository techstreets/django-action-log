# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50, null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('payload', models.TextField(default=None, null=True, blank=True)),
            ],
            options={
                'db_table': 'action_log__action_record',
            },
        ),
        migrations.CreateModel(
            name='ActionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('enabled', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'action_log__action_type',
            },
        ),
        migrations.AddField(
            model_name='actionrecord',
            name='action_type',
            field=models.ForeignKey(to='action_log.ActionType'),
        ),
    ]
