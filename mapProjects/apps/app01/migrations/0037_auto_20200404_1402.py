# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-04 06:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0036_auto_20200403_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='hutnotice',
            name='byPerson',
            field=models.CharField(default='lin', max_length=10, verbose_name='发布通知者'),
        ),
        migrations.AddField(
            model_name='hutnotice',
            name='courseEvaluateDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='通知时间'),
        ),
        migrations.AlterField(
            model_name='hutnotice',
            name='status',
            field=models.IntegerField(choices=[(1, 1), (1, 0)], default=0, verbose_name='通知状态'),
        ),
    ]
