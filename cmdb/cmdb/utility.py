from django.http import HttpResponse
import json

common_api_result = {'status':True,'msg':None,'error':None}

def Filtered_var(var):
  if var != None and len(var) > 0:
    return var
  else:
    return None

def common_api(func,request,api_result):
  result = api_result
  try:
    if request.method == "POST":
      func(request)
    else:
      pass
  except Exception as e:
    result['error'] = str(e)
  finally:
    result = json.dumps(result, indent=4)
    return HttpResponse(result, content_type="application/json")