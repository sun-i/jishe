from django.http import JsonResponse

from .models import MedicRecord


# Create your views here.

def GetMedicRecordByRecordId(request, id):
    try:
        medicRecord = MedicRecord.objects.get(recordId__exact=id)
        result = {'code': 200, 'msg': '获取病历信息成功', 'id': medicRecord.id,
                  'clinic': medicRecord.clinic , 'chief_complaint': medicRecord.chief_complaint,
                  'medical_history': medicRecord.medical_history,
                  'proposals': medicRecord.proposals,
                  'diagnosis_result': medicRecord.diagnosis_result}

        return JsonResponse(result)
    except Exception as e:
        print(e)
        result = {'code': 400, 'msg': '获取病历信息失败'}
        return JsonResponse(result)


def GenerateFinalMedicWord(request):
    if request.method == 'GET':
        result = {'code': 400, 'msg': '请求方式错误'}
        return JsonResponse(result)
    else:
        pass
