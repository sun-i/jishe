from django.db import models


# Create your models here.

class PatientProfile(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name='用户名', max_length=30, unique=True, null=False)
    password = models.CharField(verbose_name='密码', max_length=32, null=False)
    avatar = models.ImageField(verbose_name='头像', upload_to='avatars/', blank=True, null=True)
    name = models.CharField(verbose_name='姓名', null=False, max_length=100)
    phone = models.CharField(verbose_name='用户电话', max_length=20)
    email = models.EmailField(verbose_name='用户邮箱')
    card = models.CharField(verbose_name='身份证', null=True, max_length=30)
    work = models.CharField(verbose_name='工作', null=True, max_length=200)
    age = models.IntegerField(verbose_name='年龄', null=True)
    nation = models.CharField(verbose_name='国籍', null=True, max_length=200)
    address = models.CharField(verbose_name='居住地址', max_length=200, null=True)
    gender = models.CharField(verbose_name='性别', null=True, max_length=10)

    def __str__(self):
        return "患者昵称：%s" % self.username

    class Meta:
        db_table = 'patient_profile'
        verbose_name = '患者信息'
        verbose_name_plural = '患者信息'
