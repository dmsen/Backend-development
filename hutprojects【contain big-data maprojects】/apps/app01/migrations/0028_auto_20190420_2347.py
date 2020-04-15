# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-20 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0027_auto_20190420_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='alarmProcessHistory',
            fields=[
                ('alarmProcessHistoryId', models.AutoField(primary_key=True, serialize=False, verbose_name='异常处理历史id')),
                ('alarmCode', models.CharField(blank=True, max_length=16, null=True, verbose_name='异常码编号')),
                ('alarmCodeName', models.CharField(blank=True, max_length=16, null=True, verbose_name='异常码名称')),
                ('alarmSolutonId', models.CharField(blank=True, max_length=32, null=True, verbose_name='解决方案编号')),
                ('callbackMsg', models.TextField(blank=True, null=True, verbose_name='反馈信息')),
                ('processTime', models.DateTimeField(auto_now_add=True, verbose_name='处理时间')),
                ('machineName', models.DateTimeField(blank=True, max_length=16, null=True, verbose_name='机器名称')),
            ],
            options={
                'verbose_name': '异常处理历史',
                'verbose_name_plural': '异常处理历史',
                'db_table': '异常处理历史',
                'ordering': ['alarmProcessHistoryId'],
            },
        ),
        migrations.AlterField(
            model_name='alarmsolutons',
            name='alarmSolutonName',
            field=models.CharField(max_length=32, unique=True, verbose_name='解决方案名称'),
        ),
    ]
