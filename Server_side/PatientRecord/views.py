# Create your views here.
from django.http import JsonResponse

from DoctorProfile.models import DoctorProfile
from PatientProfile.models import PatientProfile
from .models import PatientRecord


def GetAllPatientRecord(request):
    pass


def GetPatientRecordByRecordId(request, id):
    try:
        record = PatientRecord.objects.get(id__exact=id)
        patient_id = record.patientId
        patient = PatientProfile.objects.get(id__exact=patient_id)
        patient_dict = {
            # 挂号单信息
            'id': record.id,
            'create_time': record.create_time,
            'reserve_time': record.reserve_time,
            'patient_name': record.patientName,
            'doctor_name': DoctorProfile.objects.get(id__exact=record.doctorId).name,
            'isFinished': record.isFinished,
            'patientRemark': record.patientRemark,
            'heartStatus': record.heartStatus,
            # 'ImagePath': AudioRecord.objects.get(id__exact=record.wavId).audioPath,
            # 病人信息
            'patient_id': patient.id,
            'name': patient.name,
            'phone': patient.phone,
            'email': patient.email,
            'card': patient.card,
            'work': patient.work,
            'age': patient.age,
            'nation': patient.nation,
            'address': patient.address,
            'gender': patient.gender
        }
        result = {'code': 200, 'msg': '查找成功', 'info': patient_dict}
        return JsonResponse(result)
    except Exception as e:
        result = {'code': 400, 'msg': '服务器繁忙，请重试'}
        return JsonResponse(result, safe=False)


def GetUnCheckedRecordByDoctorId(request, id):
    try:
        patientRecords = PatientRecord.objects.filter(doctorId__exact=id, isFinished__exact=0)
        patient_list = []
        for record in patientRecords:
            patientId = record.patientId
            patient = PatientProfile.objects.get(id__exact=patientId)
            patient_dict = {
                # 挂号单信息
                'id': record.id,
                'create_time': record.create_time,
                'reserve_time': record.reserve_time,
                'patient_name': record.patientName,
                'doctor_name': DoctorProfile.objects.get(id__exact=record.doctorId).name,
                'isFinished': record.isFinished,
                'patientRemark': record.patientRemark,
                'heartStatus': record.heartStatus,
                # 'wavPath': AudioRecord.objects.get(id__exact=record.wavId).audioPath,
                'reportWordName': record.reportWordName,
                'medicalWordName': record.medicalWordName,
                # 病人信息
                'patient_id': patient.id,
                'name': patient.name,
                'phone': patient.phone,
                'email': patient.email,
                'card': patient.card,
                'work': patient.work,
                'age': patient.age,
                'nation': patient.nation,
                'address': patient.address,
                'gender': patient.gender
            }
            patient_list.append(patient_dict)
        result = {'code': 200, 'msg': '查找成功', 'list': patient_list}

        return JsonResponse(result)

    except Exception as e:
        result = {'code': 400, 'msg': '服务器繁忙，请重试'}
        return JsonResponse(result, safe=False)


def GetAllPatientRecordByDoctorId(request, id):
    try:
        patientRecords = list(PatientRecord.objects.filter(doctorId__exact=id))
        patientRecords.sort(key=lambda k: k.isFinished)

        patient_list = []
        for record in patientRecords:
            patientId = record.patientId
            patient = PatientProfile.objects.get(id__exact=patientId)
            patient_dict = {
                # 挂号单信息
                'id': record.id,
                'create_time': record.create_time,
                'reserve_time': record.reserve_time,
                'patient_name': record.patientName,
                'doctor_name': DoctorProfile.objects.get(id__exact=record.doctorId).name,
                'isFinished': record.isFinished,
                'patientRemark': record.patientRemark,
                'heartStatus': record.heartStatus,
                # 'wavPath': AudioRecord.objects.get(id__exact=record.wavId).audioPath,
                'reportWordName': record.reportWordName,
                'medicalWordName': record.medicalWordName,
                # 病人信息
                'patient_id': patient.id,
                'name': patient.name,
                'phone': patient.phone,
                'email': patient.email,
                'card': patient.card,
                'work': patient.work,
                'age': patient.age,
                'nation': patient.nation,
                'address': patient.address,
                'gender': patient.gender
            }
            patient_list.append(patient_dict)
        result = {'code': 200, 'msg': '查找成功', 'list': patient_list}
        return JsonResponse(result)
    except Exception as e:
        result = {'code': 400, 'msg': '服务器繁忙，请重试'}
        return JsonResponse(result, safe=False)


def GetAllPatientRecordByPatientId(request, id):
    try:
        patientRecords = PatientRecord.objects.filter(patientId__exact=id)
        patient = PatientProfile.objects.get(id__exact=id)
        patient_list = []
        for record in patientRecords:
            patient_dict = {
                # 挂号单信息
                'id': record.id,
                'create_time': record.create_time,
                'reserve_time': record.reserve_time,
                'patient_name': record.patientName,
                'doctor_name': DoctorProfile.objects.get(id__exact=record.doctorId).name,
                'isFinished': record.isFinished,
                'patientRemark': record.patientRemark,
                'heartStatus': record.heartStatus,
                # 'wavPath': AudioRecord.objects.get(id__exact=record.wavId).audioPath,
                'reportWordName': record.reportWordName,
                'medicalWordName': record.medicalWordName,
                # 病人信息
                'patient_id': patient.id,
                'name': patient.name,
                'phone': patient.phone,
                'email': patient.email,
                'card': patient.card,
                'work': patient.work,
                'age': patient.age,
                'nation': patient.nation,
                'address': patient.address,
                'gender': patient.gender
            }
            patient_list.append(patient_dict)
        result = {'code': 200, 'msg': '查找成功', 'list': patient_list}
        return JsonResponse(result)
    except Exception as e:
        result = {'code': 400, 'msg': '服务器繁忙，请重试'}
        return JsonResponse(result, safe=False)


def AddPatientRecord(request):
    if request.method == 'GET':
        result = {'code': 400, 'msg': '创建方式错误'}
        return JsonResponse(result)
    else:
        try:
            print(request.POST)
            patientId = request.POST.get('patientId')
            name = request.POST.get('name')
            doctorId = request.POST.get('doctorId')
            imageId = request.POST.get('imageId')
            patientRemark = request.POST.get('remark')
            reserve_time = request.POST.get('reserve_time')

            record = PatientRecord.objects.create(doctorId=doctorId, patientId=patientId,
                                                  reserve_time=reserve_time, imageId=imageId,
                                                  patientRemark=patientRemark, patientName=name)
            record.save()
            # 创建医嘱
            # medicRecord = MedicRecord.objects.create(recordId=record.id, doctorId=doctorId, patientId=patientId)
            # medicRecord.save()
            result = {'code': 200, 'msg': '预约成功'}
            return JsonResponse(result)
        except Exception as e:
            result = {'code': 400, 'msg': '服务器繁忙，请重试'}
            return JsonResponse(result, safe=False)
