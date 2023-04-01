from django.db import models


# Create your models here.

class PatientRecord(models.Model):
    id = models.AutoField(primary_key=True)
    doctorId = models.IntegerField(verbose_name='主治医生ID', null=True)
    patientId = models.IntegerField(verbose_name='患者ID', null=True)
    patientName = models.CharField(verbose_name='患者姓名', null=True, max_length=255)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    reserve_time = models.DateTimeField(verbose_name='预约时间', null=True)
    remarks = models.TextField(verbose_name='备注', null=True)
    healthStatus = models.CharField(verbose_name='健康状态', null=True, max_length=100)
    imageId = models.IntegerField(verbose_name='图像上传记录ID', null=True)
    patientRemark = models.TextField(verbose_name='患者备注', null=True)
    reportWordName = models.CharField(verbose_name='检测报告单名字', null=True, max_length=255)
    medicalWordName = models.CharField(verbose_name='病历单名字', null=True, max_length=255)
    isFinished = models.IntegerField(verbose_name='是否生成了病例文档', default=0)

    def __str__(self):
        return "病例单: (%s)" % (self.id)

    class Meta:
        db_table = 'patient_record'
        verbose_name = '患者求诊记录'
        verbose_name_plural = '患者求诊记录'