# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-20 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20170119_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='create_user',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\u521b\u5efa\u4eba'),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_user',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\u521b\u5efa\u4eba'),
        ),
        migrations.AlterField(
            model_name='taskconf',
            name='create_user',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\u521b\u5efa\u4eba'),
        ),
        migrations.AlterField(
            model_name='taskinputparams',
            name='create_user',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\u521b\u5efa\u4eba'),
        ),
        migrations.AlterField(
            model_name='tasklog',
            name='create_user',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\u521b\u5efa\u4eba'),
        ),
    ]
