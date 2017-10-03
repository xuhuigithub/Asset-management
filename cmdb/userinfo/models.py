from django.db import models

# Create your models here.
from django.db import models

class Userinfo(models.Model):
  email = models.EmailField()
  password = models.CharField(max_length=64)


class Group(models.Model):
  name = models.CharField(max_length=30)
