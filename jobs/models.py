# coding: utf-8
from __future__ import unicode_literals

from django.db import models

from taskEngine.db import TimestampModel, DescModel, CreateUserModel


class Category(TimestampModel, CreateUserModel):
    name = models.CharField(max_length=32, verbose_name=u'分类名称')
    display = models.CharField(max_length=64, verbose_name=u'分类名称中文')

    class Meta:
        verbose_name = u'任务分类'
        verbose_name_plural = verbose_name


class Task(TimestampModel, DescModel, CreateUserModel):
    name = models.CharField(max_length=128, verbose_name=u'任务名称')
    task_type = (('shell', 'shell'), ('playbook', 'playbook'))
    type = models.CharField(max_length=16, choices=task_type)
    category = models.IntegerField(default=0)
    path = models.CharField(max_length=128, verbose_name=u'路径')

    class Meta:
        verbose_name = u'任务'
        verbose_name_plural = verbose_name

    @property
    def category_name(self):
        return Category.objects.get(pk=self.category).display


class TaskInputParams(TimestampModel, CreateUserModel):
    task_id = models.IntegerField()
    params_type = (('input', u'单行字符串'), ('text', '多行字符串'), ('int', u'整数'), ('enum', u'枚举'), ('ip', u'IP地址'))
    type = models.CharField(choices=params_type, default='input', max_length=32, verbose_name=u'任务类型')
    default = models.TextField(null=True, blank=True)
    desc = models.CharField(max_length=32, blank=True, null=True)
    required = models.BooleanField(default=False)

    class Meta:
        verbose_name = u'任务参数'
        verbose_name_plural = verbose_name


class TaskConf(TimestampModel, CreateUserModel):
    task_id = models.IntegerField()
    timeout = models.IntegerField(default=120, verbose_name=u'超时时间')
    default_user = models.CharField(max_length=32, verbose_name=u'执行用户', default='root')
    user_action = models.CharField(max_length=32, verbose_name=u'执行用户选择', choices=(('allow', 'allow'), ('deny', 'deny')))
    user_list = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = u'任务配置'
        verbose_name_plural = verbose_name


class TaskLog(TimestampModel, CreateUserModel):
    task_id = models.IntegerField(verbose_name=u'任务ID')
    hosts = models.TextField(null=True, blank=True, verbose_name=u'目标主机')
    params = models.TextField(null=True, blank=True, verbose_name=u'参数')

    class Meta:
        verbose_name = u'任务日志'
        verbose_name_plural = verbose_name
