# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-14 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0014_auto_20190413_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='gateways_all',
            fields=[
                ('gatewayId', models.AutoField(primary_key=True, serialize=False, verbose_name='网关Id')),
                ('gatewayName', models.CharField(max_length=30, verbose_name='网关名')),
            ],
            options={
                'verbose_name': '所有网关',
                'verbose_name_plural': '所有网关',
                'db_table': '所有网关',
                'ordering': ['gatewayId'],
            },
        ),
        migrations.CreateModel(
            name='IOPoints',
            fields=[
                ('IOPName', models.AutoField(primary_key=True, serialize=False, verbose_name='监测点id')),
            ],
        ),
        migrations.CreateModel(
            name='IOPoints_all',
            fields=[
                ('IOPId', models.AutoField(primary_key=True, serialize=False, verbose_name='监测点')),
                ('IOPName', models.CharField(max_length=30, verbose_name='监测点名')),
            ],
            options={
                'verbose_name': '所有监测点',
                'verbose_name_plural': '所有监测点',
                'db_table': '所有监测点',
                'ordering': ['IOPId'],
            },
        ),
        migrations.AddField(
            model_name='gateways_all',
            name='IOPNames',
            field=models.ManyToManyField(related_name='iopname', to='app01.IOPoints_all', verbose_name='监测点名'),
        ),
    ]
