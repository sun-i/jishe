import time

import jwt
from django.http import JsonResponse

from Server_side.settings import JWT_TOKEN_KEY
from .models import DoctorProfile


# Create your views here.

def GetAllDoctors(request):
    try:
        doctors = DoctorProfile.objects.all()
        doctor_list = []
        for doctor in doctors:
            doctor_dict = {'id': doctor.id, 'username': doctor.username, 'name': doctor.name, 'phone': doctor.phone,
                           'email': doctor.email, 'address': doctor.address, 'age': doctor.age}
            doctor_list.append(doctor_dict)
        result = {'code': 200, 'msg': '查询医生信息成功', 'list': doctor_list}
        return JsonResponse(result)
    except Exception as e:
        result = {'code': 400, 'msg': '查询医生信息失败'}
        return JsonResponse(result)


# 医生登录
def DoctorLogin(request):
    if request.method == 'GET':
        result = {'code': 400, 'error': 'doctor登录方式错误'}
        return JsonResponse(result)
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            doctor = DoctorProfile.objects.get(username__exact=username, password__exact=password)
            doctor.save()
        except Exception as e:
            result = {'code': 400, 'status': 'ERROR', 'msg': '该用户不存在'}
            return JsonResponse(result)

        # 此处说明登录成功了
        now_t = time.time()
        # 登录状态保持1天

        token_data = {'username': username, 'exp': now_t + 3600 * 24}

        token = jwt.encode(token_data, JWT_TOKEN_KEY, algorithm='HS256')

        result = {'code': 200, 'status': 'OK', 'msg': '登录成功', 'token': token,
                  'id': doctor.id, 'username': doctor.username, 'name': doctor.name, 'phone': doctor.phone,
                  'email': doctor.email, 'address': doctor.address, 'age': doctor.age, 'card': doctor.card,
                  'gender': doctor.gender}

        return JsonResponse(result)


# 用户注册
def DoctorRegister(request):
    if request.method == 'GET':
        result = {'code': 400, 'error': '注册方式错误'}
        return JsonResponse(result)
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = DoctorProfile.objects.filter(username__exact=username)
        except Exception as e:
            print(e)
            result = {'code': 400, 'msg': '系统繁忙，请重试'}
            return JsonResponse(result, safe=False)

        if user:
            result = {'code': 400, 'msg': '用户名已存在'}
            return JsonResponse(result, safe=False)
        else:
            try:
                doctor = DoctorProfile.objects.create(username=username, password=password, name=name)
                doctor.save()
                print(doctor)
                result = {'code': 200, 'status': 'OK', 'msg': '用户注册成功'}
                return JsonResponse(result, safe=False)
            except Exception as e:
                result = {'code': 400, 'status': 'ERROR', 'msg': '操作繁忙，请重试'}
                return JsonResponse(result, safe=False)


# 校验用户登录状态
def AuthDoctorInfo(request):
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
            doctor = DoctorProfile.objects.get(username__exact=prop.get('username'))
            result = {'code': 200, 'status': 'OK', 'msg': '身份校验成功', 'token': token,
                      'id': doctor.id, 'username': doctor.username}
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

            doctor = DoctorProfile.objects.get(id=id)
            doctor.email = email
            doctor.address = address
            doctor.phone = phone
            doctor.nation = nation
            doctor.card = card
            doctor.work = work
            doctor.age = age
            doctor.gender = gender

            doctor.save()
            result = {'code': 200, 'status': 'OK', 'msg': '身份修改成功'}

            return JsonResponse(result)
        except Exception as e:
            result = {'code': 400, 'error': '修改信息错误'}
            return JsonResponse(result)
