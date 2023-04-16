import base64
import hashlib
import json
import os
import uuid

from django.http import JsonResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from docx.shared import Inches
from docxtpl import DocxTemplate, InlineImage
from django.conf import settings

from Detection.nets.u_net import U_Net
from DoctorProfile.models import DoctorProfile
from MedicRecord.models import MedicRecord
from PatientProfile.models import PatientProfile
from PatientRecord.models import PatientRecord
from Detection.utils.unet import Unet
from PIL import Image


# 获得随机的文档名字


def get_random_str():
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode('utf-8')
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()


def load_image(request):
    if request.method == "GET":
        result = {'code': 400, 'error': '上传图片方式错误'}
        return JsonResponse(result)
    else:
        file_path = request.POST.get("img_path")
        print(file_path)
        try:
            unet = U_Net()
            prob, pred = unet.predict(file_path)
            print("success")

            # 将返回的图像保存到本地文件
            save_path = file_path.rstrip(".png") + '_result.png'
            pred.save(save_path)

            # 将保存的文件读取并编码为 base64 格式的字符串
            with open(save_path, 'rb') as f:
                imgData = base64.b64encode(f.read()).decode('ascii')
            result = {'code': 200, 'msg': '上传图片成功', 'data': imgData, 'prob': prob}
            return JsonResponse(result)
        except Exception as e:
            print(e)
            result = {'code': 400, 'error': '上传图片失败'}
            return JsonResponse(result)

            # 将保存的文件读取并编码为 base64 格式的字符串
            with open(save_path, 'rb') as f:
                imgData = base64.b64encode(f.read()).decode('ascii')
            result = {'code': 200, 'msg': '上传图片成功', 'data': imgData}
            return JsonResponse(result)
        except Exception as e:
            print(e)
            result = {'code': 400, 'error': '上传图片失败'}
            return JsonResponse(result)


@csrf_exempt
def DownloadFile(request):
    print('Hello')
    filename = request.GET.get('filename')
    baseUrl = os.path.join(settings.MEDIA_ROOT, 'words')
    filepath = os.path.join(baseUrl, filename)
    fp = open(filepath, 'rb')
    response = StreamingHttpResponse(fp)

    print('headers: ', request.headers.get('Origin'))
    response['Access-Control-Allow-Origin'] = request.headers.get('Origin')
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"' % filename
    print('response: ', response['Access-Control-Allow-Origin'])
    return response


def GenerateReportWord(request):
    if request.method == 'GET':
        result = {'code': 400, 'msg': '请求方式错误'}
        return JsonResponse(result)
    else:
        try:
            recordId = request.POST.get('recordId')

            record = PatientRecord.objects.get(id__exact=recordId)
            patient = PatientProfile.objects.get(id__exact=record.patientId)

            d1 = request.POST.get('d1')
            d2 = request.POST.get('d2')
            path = request.POST.get('img_path')
            path2 = path.rstrip(".png") + '_result.png'
            baseUrl = os.path.join(settings.MEDIA_ROOT, 'words')
            assetUrl = os.path.join(baseUrl, 'ReportTemplate.docx')
            tpl = DocxTemplate(assetUrl)

            context = {'d1': d1, 'd2': d2, 'img1': InlineImage(tpl, path, width=Inches(2.0)),
                       'img2': InlineImage(tpl, path2, width=Inches(2.0)),
                       'name': patient.name, 'nation': patient.nation, 'email': patient.email, 'age': patient.age,
                       'address': patient.address, 'card': patient.card, 'phone': patient.phone,
                       'gender': patient.gender, 'time': record.reserve_time}

            tpl.render(context)
            reportName = get_random_str() + '.docx'

            tpl.save(os.path.join(baseUrl, reportName))
            record.reportWordName = reportName
            record.save()

            return JsonResponse({'code': 200, 'msg': '生成文档成功'})

        except Exception as e:
            print(e)
            result = {'code': 400, 'msg': '生成文档失败'}
            return JsonResponse(result)


def GenerateMedicWord(request):
    if request.method == 'GET':
        result = {'code': 400, 'msg': '请求方式错误'}
        return JsonResponse(result)
    else:
        try:
            recordId = request.POST.get('recordId')
            medicRecord = MedicRecord.objects.get(recordId__exact=recordId)
            print(request.POST)
            record = PatientRecord.objects.get(id__exact=recordId)
            patient = PatientProfile.objects.get(id__exact=record.patientId)
            a1 = request.POST.get('a1')
            a2 = request.POST.get('a2')
            a3 = request.POST.get('a3')
            a4 = request.POST.get('a4')
            a5 = request.POST.get('a5')
            a6 = request.POST.get('a6')
            a7 = DoctorProfile.objects.get(id__exact=record.doctorId).name
            medicRecord.clinic = a2
            medicRecord.chief_complaint = a3
            medicRecord.medical_history = a4
            medicRecord.proposals = a5
            medicRecord.diagnosis_result = a6
            medicRecord.save()

            baseUrl = os.path.join(settings.MEDIA_ROOT, 'words')
            assetUrl = os.path.join(baseUrl, 'MedicTemplate.docx')
            tpl = DocxTemplate(assetUrl)

            context = {'a1': a1, 'a2': a2, 'a3': a3, 'a4': a4, 'a5': a5, 'a6': a6, 'a7': a7,
                       'name': patient.name, 'nation': patient.nation, 'email': patient.email, 'age': patient.age,
                       'address': patient.address, 'card': patient.card, 'phone': patient.phone,
                       'gender': patient.gender, 'time': record.reserve_time
                       }
            tpl.render(context)

            medicName = get_random_str() + '.docx'

            tpl.save(os.path.join(baseUrl, medicName))
            record.medicalWordName = medicName
            record.save()
            if record.reportWordName:
                record.isFinished = 1
                record.save()

            return JsonResponse({'code': 200, 'msg': '生成文档成功'})
        except Exception as e:
            print(e)
            result = {'code': 400, 'msg': '生成文档失败'}
            return JsonResponse(result)
