# -*- coding: utf-8 -*-
from hashlib import sha256 as sha
from .models import Userinfo
import re
from functools import wraps
from django.http import HttpResponseRedirect

def Hash(value):
  sha_hash = sha()
  sha_hash.update(value)
  result = sha_hash.hexdigest()
  return result


def authenticate(identity,password):
  data = {}
  data['password'] = password
  email_regexp = re.compile(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b')
  email = email_regexp.findall(str(identity))
  if len(email) > 0:
    data['email'] = identity
  else:
    data['username'] = identity
  try:
    user = Userinfo.objects.get(**data)
  except Userinfo.DoesNotExist:
    return None
  else:
    return user


def login(request,user):
  try:
    assert request.session['member_id'] == user.id
  except Exception:
    request.session['member_id'] = user.id
#admin 用户登录 留下一个session在客户端，当admin用户不logout切换用户登录时，会导致session中的['member_id']仍是admin用户的
#所以做一个判断 如果两次的id不一致则，重置session中的member_id

def login_required(loginurl):
  def outer(func):
    @wraps(func)
    def wrapper(request,*args,**kwargs):
      if request.session.get('member_id'):
        return func(request, *args, **kwargs)
      else:
        return HttpResponseRedirect(loginurl)
    return wrapper
  return outer