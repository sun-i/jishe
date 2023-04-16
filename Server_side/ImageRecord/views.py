import base64
import hashlib
import os
import uuid

import cv2
import numpy as np
from django.conf import settings
from django.http import JsonResponse
from PatientRecord.models import PatientRecord
from .models import ImageRecord


# 获得随机的照片名字
def get_random_str():
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode('utf-8')
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()


# 上传图像文件
def UploadImage(request):
    if request.method == 'GET':
        result = {'code': 400, 'error': '上传图片方式错误'}
        return JsonResponse(result)
    else:
        image_file = request.FILES.get('image')
        username = request.POST.get('username')
        suffix = os.path.splitext(image_file.name)[1]
        file_type = suffix[1:]
        print(file_type)
        if file_type not in ["png", "jpg"] or not username:
            return JsonResponse({'code': 400, 'msg': '图片文件上传错误'})

        image_name = get_random_str()  # 随机生成一个图片的名称
        file_path = os.path.join(settings.MEDIA_ROOT, image_name + suffix)

        try:
            f = open(file_path, 'wb')
            for data_block in image_file.chunks():
                f.write(data_block)
            f.close()

            record = ImageRecord.objects.create(imageUserName=username,
                                                imageName=image_name + os.path.splitext(image_file.name)[1],
                                                imagePath=file_path,
                                                imageUrl=file_path)
            record.save()
            result = {'code': 200, 'msg': '图片文件写入成功', 'imageId': int(record.id)}
            print(result)
            return JsonResponse(result, safe=False)
        except Exception as e:
            result = {'code': 400, 'msg': '图片文件上传失败！'}
            return JsonResponse(result)


# 读取图像文件
def read_part_image(filename, target_size=(224, 224)):
    # Load image
    image = cv2.imread(filename)

    # Resize image
    image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)

    # Convert image to array and normalize
    image = np.array(image, dtype=np.float32)
    image /= 255.0

    return image


def ReadImage(request):
    if request.method == 'GET':
        result = {'code': 400, 'error': '读取图片方式错误'}
        return JsonResponse(result)
    else:
        try:
            id = request.POST.get('id')
            imgId = PatientRecord.objects.get(id__exact=id).imageId
            img = ImageRecord.objects.get(id__exact=imgId)
            imgName = img.imageName
            imgPath = os.path.join(settings.MEDIA_ROOT, imgName)
            with open(imgPath, 'rb') as f:
                image_data = base64.b64encode(f.read()).decode('utf-8')
            print(imgPath)
            imgPath2 = imgPath.rstrip(".png") + '_result.png'
            if os.path.exists(imgPath2):
                with open(imgPath2, 'rb') as f:
                    image_data2 = base64.b64encode(f.read()).decode('utf-8')
                result = {'code': 200, 'msg': '图片文件读取成功！', 'img_data': image_data, 'img_data2': image_data2, 'img_path': imgPath}
            else:
                result = {'code': 200, 'msg': '图片文件读取成功！', 'img_data': image_data, 'img_path': imgPath}
            return JsonResponse(result)
        except Exception as e:
            print(e)
            result = {'code': 400, 'msg': '读取图片文件失败'}
            return JsonResponse(result)
