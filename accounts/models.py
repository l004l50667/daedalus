# coding: utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

from taskEngine.db import TimestampModel, DescModel


class Department(TimestampModel, DescModel):
    name = models.CharField(max_length=32, verbose_name=u'部门')

    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = verbose_name


class UserProfile(AbstractUser):
    department = models.IntegerField()
