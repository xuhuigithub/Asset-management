from django.shortcuts import render

# Create your views here.
from .models import Group
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .utility import authenticate as my_authenticate
from .utility import login_required as my_login_required
from cmdb.utility import common_api_result
from django.views.decorators.csrf import csrf_exempt



def Login(request):
  result = {"status":True,"msg":None,"error":None}
  try:
    user = authenticate(username='xuhui',password='123456')
    if user is not None:
      if user.is_active:
        result["msg"] = "User is valid,active and authenticated"
        login(request,user)
      else:
        result["msg"] = "The account has been disabled"
    else:
      result["msg"] = "Username or Password was invaild"
  except Exception as e:
    result['error'] = str(e)
  finally:
    result = json.dumps(result,indent=4)
    return HttpResponse(result,content_type="application/json")

@login_required
def Logout(request):
  try:
    logout(request)
  except Exception,e:
    return HttpResponse('error %s' %e)
  else:
    return HttpResponse('ok')



@csrf_exempt
def Login_t(request):
  result = common_api_result.copy()
  if request.method == 'GET':
    data = request.GET.dict()
    identity = data.get('username')
    password = data.get('password')
    user = my_authenticate(identity,password)
    if user is not None:
      if user.is_actived:
        try:
          assert request.session['member_id'] == user.id
        except KeyError:
          request.session['member_id'] = user.id
          result['msg'] = 'ok'
        except AssertionError:
          request.session['member_id'] = user.id
          result['msg'] = 'logout and login ok'
        else:
          result['msg'] = 'You alerdy logind'
      else:
          result['error'] = 'The account has been disabled'
    else:
      result['error'] = "Username or Password was invaild"
  result = json.dumps(result, indent=4)
  return HttpResponse(result, content_type="application/json")

@my_login_required('/test_login')
def Logout_t(request):
  result = common_api_result.copy()
  try:
    request.session['member_id']
    request.session.flush()
    result['msg'] = 'ok'
  except KeyError:
    result['msg'] = 'Pls login first'
  finally:
    result = json.dumps(result, indent=4)
    return HttpResponse(result, content_type="application/json")
