# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from userinfo.models import Group

# Create your models here.
class Hostinfo(models.Model):
  name = models.CharField(max_length=30)
  ip_addr = models.CharField(max_length=20)
  ipmi_addr = models.CharField(max_length=20)
  password = models.CharField(max_length=64)
  owner_group = models.ForeignKey(Group)
  #默认的 django.db.models.ForeignKey.on_delete set to CASCADE 也就是在这个数据模型中，当你的组被删除后，你所有的属于这个组的主机也同样会被删除