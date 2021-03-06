# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-13 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0013_auto_20190413_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='customerName',
            field=models.CharField(max_length=10, unique=True, verbose_name='顾客名'),
        ),
        migrations.AlterField(
            model_name='machines',
            name='machineName',
            field=models.CharField(max_length=10, unique=True, verbose_name='机器名称'),
        ),
        migrations.AlterField(
            model_name='machtypes',
            name='machTypeName',
            field=models.CharField(max_length=10, unique=True, verbose_name='机器类型名称'),
        ),
        migrations.AlterField(
            model_name='users',
            name='userName',
            field=models.CharField(max_length=10, unique=True, verbose_name='用户名'),
        ),
    ]
