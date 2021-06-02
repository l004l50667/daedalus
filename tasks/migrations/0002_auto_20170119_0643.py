# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-19 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u4efb\u52a1\u5206\u7c7b', 'verbose_name_plural': '\u4efb\u52a1\u5206\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': '\u4efb\u52a1', 'verbose_name_plural': '\u4efb\u52a1'},
        ),
        migrations.AlterModelOptions(
            name='taskconf',
            options={'verbose_name': '\u4efb\u52a1\u914d\u7f6e', 'verbose_name_plural': '\u4efb\u52a1\u914d\u7f6e'},
        ),
        migrations.AlterModelOptions(
            name='taskinputparams',
            options={'verbose_name': '\u4efb\u52a1\u53c2\u6570', 'verbose_name_plural': '\u4efb\u52a1\u53c2\u6570'},
        ),
        migrations.AlterModelOptions(
            name='tasklog',
            options={'verbose_name': '\u4efb\u52a1\u65e5\u5fd7', 'verbose_name_plural': '\u4efb\u52a1\u65e5\u5fd7'},
        ),
        migrations.AddField(
            model_name='category',
            name='display',
            field=models.CharField(default='', max_length=64, verbose_name='\u5206\u7c7b\u540d\u79f0'),
            preserve_default=False,
        ),
    ]