# coding: utf-8

from django.db import models


class TimestampModel(models.Model):
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class DescModel(models.Model):
    desc = models.CharField(max_length=32, verbose_name=u'描述', blank=True, null=True)

    class Meta:
        abstract = True


class CreateUserModel(models.Model):
    create_user = models.CharField(max_length=32, verbose_name=u'创建人')

    class Meta:
        abstract = True
