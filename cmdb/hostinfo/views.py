
from django.shortcuts import render

# Create your views here.
from .models import Hostinfo
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cmdb.utility import Filtered_var
  
def index(request):
  context = {}
  host_list = Hostinfo.objects.all()
  context['host_list'] = host_list
  return render(request,'data_table.html',context)

@csrf_exempt 
def add_host(request):
  result = {'status':True,'msg':None,'error':None}
  try:
    request.encoding='utf-8'
    data = request.POST.dict()
    name = Filtered_var(data.get('name'))
    print name
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
    result = json.dumps(result,indent=4)
    return HttpResponse(result, content_type="application/json")
  