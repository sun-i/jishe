from django.db import models

# Create your models here.

class MedicRecord(models.Model):
    id = models.AutoField(primary_key=True) # 门诊号
    recordId = models.IntegerField(verbose_name='挂号记录ID', null=True)
    patientId = models.IntegerField(verbose_name='患者ID', null=True)
    doctorId = models.IntegerField(verbose_name='医生ID', null=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    clinic = models.CharField(verbose_name='科室', default='心脏科室', null=True, max_length=200)
    chief_complaint = models.TextField(verbose_name='主诉', null=True)
    medical_history = models.TextField(verbose_name='既往病史', null=True)
    proposals = models.TextField(verbose_name='医嘱', null=True)
    diagnosis_result = models.TextField(verbose_name='诊断结果', null=True)

    def __str__(self):
        return "医嘱ID：%s" % (self.id)

    class Meta:
        db_table = 'medic_record'
        verbose_name = '医嘱信息'
        verbose_name_plural = '医嘱信息'