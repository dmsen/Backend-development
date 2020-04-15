# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-16 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0018_auto_20190416_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iopoints',
            name='aline',
            field=models.IntegerField(blank=True, null=True, verbose_name='校准值'),
        ),
        migrations.AlterField(
            model_name='iopoints',
            name='maxRange',
            field=models.IntegerField(verbose_name='最大量程'),
        ),
        migrations.AlterField(
            model_name='iopoints',
            name='method',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='计算方式'),
        ),
    ]
