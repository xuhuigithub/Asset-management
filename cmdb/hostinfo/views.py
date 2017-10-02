# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from .models import Hostinfo
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cmdb.utility import Filtered_var
from functools import wraps



def index(request):
  context = {}
  host_list = Hostinfo.objects.all()
  context['host_list'] = host_list
  return render(request,'data_table.html',context)



class Host():
  def __init__(self):
    self.result = {'status':True,'msg':None,'error':None}
    self.encoding = 'utf-8'

  def jungle(method):
    def outer(func):
      @wraps(func)
      def wrapper(self,request,*args,**kwargs):
        if request.method == method:
          return f(request,*args,**kwargs)
        else:
          return HttpResponse('EOF')
      return wrapper
    return outer
  
  def add(self,request):
    result = self.result
    if request.POST:
      try:
        request.encoding = self.encoding
        data = request.POST.dict()
        name = Filtered_var(data.get('name'))
        ip_addr = Filtered_var(data.get('ip_addr'))
        password = Filtered_var(data.get('password'))
        ipmi_addr = Filtered_var(data.get('ipmi_addr'))
        Hostinfo.objects.create(**{'name':name,
                                   'ip_addr': ip_addr,
                                   'ipmi_addr': ipmi_addr,
                                   'password': password,
                                   })
      except Exception,e:
        result['error'] = str(e)
      else:
        result['msg'] = 'ok'
      finally:
        result = json.dumps(self.result,indent=4)
        return HttpResponse(result, content_type="application/json")
    else:
      result['msg'] = 'Only post method'
      result = json.dumps(self.result,indent=4)
      return HttpResponse(result, content_type="application/json")
  
  @jungle('POST')
  def delete(self,request):
    result = self.result
    try:
      data = request.POST.dict()
      record = Hostinfo.objects.get(**data)
      record.delet()
    except Exception,e:
      result['error'] = str(e)
    else:
      result['msg'] = 'ok'
    finally:
      result = json.dumps(self.result,indent=4)
      return HttpResponse(result, content_type="application/json")
  
  def update(self,request):
    result = self.result
    try:
      data = request.POST.dict()
      id = data['id']
      record = Hostinfo.objects.get(id).update(**data)
    except Exception,e:
      result['error'] = str(e)
    else:
      result['msg'] = 'ok'
    finally:
      result = json.dumps(self.result,indent=4)
      return HttpResponse(result, content_type="application/json")
    
      
      
  