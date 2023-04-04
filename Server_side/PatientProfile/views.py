import time

import jwt
from django.http import JsonResponse

# Create your views here.
# 患者登录
from Server_side.settings import JWT_TOKEN_KEY
from .models import PatientProfile


def PatientLogin(request):
    if request.method == 'GET':
        result = {'code': 400, 'error': 'patient登录方式错误'}
        return JsonResponse(result)
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST)

        try:
            patient = PatientProfile.objects.get(username__exact=username, password__exact=password)
            patient.save()
        except Exception as e:
            print(e)
            result = {'code': 400, 'status': 'ERROR', 'msg': '该用户不存在'}
            return JsonResponse(result)

        # 此处说明登录成功了
        now_t = time.time()
        # 登录状态保持1天
        token_data = {'username': username, 'exp': now_t + 3600 * 24}

        token = jwt.encode(token_data, JWT_TOKEN_KEY, algorithm='HS256')

        result = {'code': 200, 'status': 'OK', 'msg': '登录成功', 'token': token,
                  'id': patient.id, 'username': patient.username, 'name': patient.name, 'phone': patient.phone,
                  'email': patient.email, 'address': patient.address, 'nation': patient.nation,
                  'age': patient.age, 'card': patient.card, 'gender': patient.gender}

        return JsonResponse(result)


# 患者注册
def PatientRegister(request):
    if request.method == 'GET':
        result = {'code': 400, 'error': '注册方式错误'}
        return JsonResponse(result)
    else:
        username = request.POST.get('username')
        # print(request.POST)
        password = request.POST.get('password')

        try:
            user = PatientProfile.objects.filter(username__exact=username)
        except Exception as e:
            # print(e)
            result = {'code': 400, 'msg': '系统繁忙，请重试'}
            return JsonResponse(result, safe=False)

        if user:
            result = {'code': 400, 'msg': '用户名已存在'}
            return JsonResponse(result, safe=False)
        else:
            try:
                patient = PatientProfile.objects.create(username=username, password=password)
                patient.save()
                print(patient)
                result = {'code': 200, 'status': 'OK', 'msg': '用户注册成功'}
                return JsonResponse(result, safe=False)
            except Exception as e:
                print(e)
                result = {'code': 400, 'status': 'ERROR', 'msg': '操作繁忙，请重试'}
                return JsonResponse(result, safe=False)


# 校验用户登录状态
def AuthPatientInfo(request):
    if request.method == 'GET':
        result = {'code': 400, 'error': '验证方式错误'}
        return JsonResponse(result, safe=False)
    else:
        token = request.META.get('HTTP_AUTHORIZATION')  # 从请求头获得Authorization对应的值
        if not token:
            result = {'code': 400, 'error': '验证不存在，请重新登录！'}
            return JsonResponse(result, safe=False)

        try:
            prop = jwt.decode(token, JWT_TOKEN_KEY, algorithms='HS256')
        except Exception as e:
            result = {'code': 400, 'error': '验证过期，请重新登录！'}
            return JsonResponse(result, safe=False)

            # 如果执行到这个地方 说明token验证成功
        try:
            patient = PatientProfile.objects.get(username__exact=prop.get('username'))
            result = {'code': 200, 'status': 'OK', 'msg': '身份校验成功', 'token': token,
                      'id': patient.id, 'username': patient.username}
            return JsonResponse(result, safe=False)
        except Exception as e:
            result = {'code': 400, 'error': '认证失败，请重新登录！'}
            return JsonResponse(result, safe=False)


def ModifyInfo(request):
    if request.method == 'GET':
        result = {'code': 400, 'error': '修改方式错误'}
        return JsonResponse(result, safe=False)
    else:
        try:
            id = int(request.POST.get('id'))
            card = request.POST.get('card')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            nation = request.POST.get('nation')
            work = request.POST.get('work')
            age = request.POST.get('age')
            gender = request.POST.get('gender')

            patient = PatientProfile.objects.get(id=id)
            patient.email = email
            patient.address = address
            patient.phone = phone
            patient.nation = nation
            patient.card = card
            patient.work = work
            patient.age = age
            patient.gender = gender

            patient.save()
            result = {'code': 200, 'status': 'OK', 'msg': '信息修改成功'}

            return JsonResponse(result)
        except Exception as e:
            result = {'code': 400, 'error': '修改信息错误'}
            return JsonResponse(result)

# Create your views here.
