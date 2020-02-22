# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-19 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0023_auto_20190417_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='singleAlarmCodes',
            fields=[
                ('singleAlarmCodeId', models.AutoField(primary_key=True, serialize=False, verbose_name='单个异常记录id')),
                ('startTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间')),
                ('duration', models.IntegerField(blank=True, default=10, null=True, verbose_name='持续时间')),
                ('singleAlarmCodeStatus', models.IntegerField(default=0, verbose_name='异常记录状态')),
                ('alarmCodeName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.alarmCodes', verbose_name='异常码名字')),
                ('machineName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.machines', verbose_name='机器名')),
            ],
            options={
                'verbose_name': '单个异常记录',
                'verbose_name_plural': '单个异常记录',
                'db_table': '单个异常记录',
                'ordering': ['singleAlarmCodeId'],
            },
        ),
    ]
