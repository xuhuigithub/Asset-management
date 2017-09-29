from hostinfo.models import Hostinfo 
from django.http import HttpResponse
import json

def get_all(request):
  result = {'data':[]}
  all = Hostinfo.objects.all()
  for i in all:
    result['data'].append({'id':i.id,'hostname':i.name,'ip_address':i.ip_addr,'ipmi_address':i.ipmi_addr,'password':i.password})
  result = json.dumps(result,sort_keys=True,indent=4)
  print result
  return HttpResponse(result, content_type="application/json")

def update_one(request):
  result = {'status':True,'msg':None,'error':None}
  id = 1
  try:
    Hostinfo.objects.filter(id=id).update(**{'name':'mongo3',
                                           'ip_addr':'192.168.1.3',
                                           'ipmi_addr':'192.168.1.3',
                                           'password':'123456',
                                           })
  except Exception as e:
    result['msg'] = e
    result['error']=True
  else:
    result['msg'] = 'ok'
  result = json.dumps(result,sort_keys=True,indent=4) 
  return HttpResponse(result, content_type="application/json")