# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-21 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20180820_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid_name', models.CharField(max_length=128, verbose_name='导航名')),
                ('guid_enable', models.BooleanField(default=True, verbose_name='是否启用')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Tag', verbose_name='相关tag')),
            ],
            options={
                'verbose_name': '导航信息',
                'verbose_name_plural': '导航信息',
            },
        ),
        migrations.AlterModelOptions(
            name='informationclassification',
            options={'verbose_name': '项目分类', 'verbose_name_plural': '项目分类'},
        ),
        migrations.AlterField(
            model_name='article',
            name='article_information_classification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.InformationClassification', verbose_name='项目分类'),
        ),
        migrations.AlterField(
            model_name='informationclassification',
            name='info_name_cn',
            field=models.CharField(max_length=128, verbose_name='项目分类cn'),
        ),
        migrations.AlterField(
            model_name='informationclassification',
            name='info_name_en',
            field=models.CharField(max_length=128, verbose_name='项目分类en'),
        ),
    ]
