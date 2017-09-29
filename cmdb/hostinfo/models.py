from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hostinfo(models.Model):
  name = models.CharField(max_length=30)
  ip_addr = models.CharField(max_length=20)
  ipmi_addr = models.CharField(max_length=20)
  password = models.CharField(max_length=64)
  