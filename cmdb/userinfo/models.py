from django.db import models

# Create your models here.
from django.db import models
class Group(models.Model):
  name = models.CharField(max_length=30)

class Userinfo(models.Model):
  # REQUIRED_FIELDS = ('email','password',)
  # USERNAME_FIELD = 'username'
  username = models.CharField(max_length=32,unique=True)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=64)
  is_actived = models.BooleanField(default=True)
  group = models.ManyToManyField('Group')



