# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-13 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_auto_20190413_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machines',
            name='dataOfProdect',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='生产日期'),
        ),
    ]
