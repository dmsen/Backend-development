# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-05 10:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_notice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'verbose_name': '公告', 'verbose_name_plural': '公告'},
        ),
    ]