# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-18 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('create_user', models.CharField(max_length=32, verbose_name='\u521b\u5efa\u4eba')),
                ('name', models.CharField(max_length=32, verbose_name='\u5206\u7c7b\u540d\u79f0')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('desc', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u63cf\u8ff0')),
                ('create_user', models.CharField(max_length=32, verbose_name='\u521b\u5efa\u4eba')),
                ('name', models.CharField(max_length=128, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('type', models.CharField(choices=[('shell', 'shell'), ('playbook', 'playbook')], max_length=16)),
                ('category', models.IntegerField(default=0)),
                ('path', models.CharField(max_length=64, verbose_name='\u8def\u5f84')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('create_user', models.CharField(max_length=32, verbose_name='\u521b\u5efa\u4eba')),
                ('timeout', models.IntegerField(default=0, verbose_name='\u8d85\u65f6\u65f6\u95f4')),
                ('exc_user', models.CharField(default='root', max_length=32, verbose_name='\u6267\u884c\u7528\u6237')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskInputParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('create_user', models.CharField(max_length=32, verbose_name='\u521b\u5efa\u4eba')),
                ('task_id', models.IntegerField()),
                ('type', models.CharField(choices=[('input', '\u5355\u884c\u5b57\u7b26\u4e32'), ('text', '\u591a\u884c\u5b57\u7b26\u4e32'), ('int', '\u6574\u6570'), ('enum', '\u679a\u4e3e'), ('ip', 'IP\u5730\u5740')], default='input', max_length=32, verbose_name='\u4efb\u52a1\u7c7b\u578b')),
                ('default', models.TextField(blank=True, null=True)),
                ('desc', models.CharField(blank=True, max_length=32, null=True)),
                ('required', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('create_user', models.CharField(max_length=32, verbose_name='\u521b\u5efa\u4eba')),
                ('task_id', models.IntegerField(verbose_name='\u4efb\u52a1ID')),
                ('hosts', models.TextField(blank=True, null=True, verbose_name='\u76ee\u6807\u4e3b\u673a')),
                ('params', models.TextField(blank=True, null=True, verbose_name='\u53c2\u6570')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
