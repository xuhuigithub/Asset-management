# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from .models import Hostinfo
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cmdb.utility import Filtered_var
from functools import wraps
from userinfo.models import Group



def index(request):
  context = {}
  host_list = Hostinfo.objects.all()
  group_list = Group.objects.all()
  context['host_list'] = host_list
  context['group_list'] = group_list
  return render(request,'data_table.html',context)


def jungle(method):
  def outer(func):
    @wraps(func)
    def wrapper(self,request,*args,**kwargs):
      if request.method == method:
        return func(self,request,*args,**kwargs)
      else:
        return HttpResponse('EOF')
    return wrapper
  return outer

class Host():
  def __init__(self):
    self.result = {'status':True,'msg':None,'error':None}
    self.encoding = 'utf-8'

  
  def Add(self,request):
    result = self.result
    if request.POST:
      try:
        request.encoding = self.encoding
        data = request.POST.dict()
        name = Filtered_var(data.get('name'))
        ip_addr = Filtered_var(data.get('ip_addr'))
        password = Filtered_var(data.get('password'))
        ipmi_addr = Filtered_var(data.get('ipmi_addr'))
        owner_group_id = Filtered_var(data.get('owner_group'))
        owner_group = Group.objects.get(id=owner_group_id)
        Hostinfo.objects.create(**{'name':name,
                                   'ip_addr': ip_addr,
                                   'ipmi_addr': ipmi_addr,
                                   'password': password,
                                   'owner_group': owner_group,
                                   })
      except Exception,e:
        result['error'] = str(e)
      else:
        result['msg'] = 'ok'
      finally:
        result = json.dumps(result,indent=4)
        return HttpResponse(result, content_type="application/json")
    else:
      result['msg'] = 'Only post method'
      result = json.dumps(self.result,indent=4)
      return HttpResponse(result, content_type="application/json")
  
  @jungle('POST')
  def Delete(self,request):
    result = self.result
    try:
      data = request.POST.dict()
      record = Hostinfo.objects.get(id=data.get('id'),name=data.get('name'))
      record.delete()
    except Exception,e:
      result['error'] = str(e)
    else:
      result['msg'] = 'ok'
    finally:
      print result
      result = json.dumps(result,indent=4)
      return HttpResponse(result, content_type="application/json")

  @jungle('POST')
  def Update(self,request):
    result = self.result
    try:
      data = request.POST.dict()
      id = data.get('id')
      record = Hostinfo.objects.filter(id=id)
      #get filter 的区别 filter返回的是所有符合条件的数据（无论如何返回列表），而get返回的是单一数据，相当于filter(id=id).first()
      owner_group_id = Filtered_var(data.get('owner_group'))
      owner_group = Group.objects.get(id=owner_group_id)
      data['owner_group'] = owner_group
      record.update(**data)
    except Exception,e:
      result['error'] = str(e)
    else:
      result['msg'] = 'ok'
    finally:
      result = json.dumps(result,indent=4)
      print result
      return HttpResponse(result, content_type="application/json")

    
      
      
  