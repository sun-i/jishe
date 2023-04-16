from django.db import models


class DoctorProfile(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name='用户名', max_length=30, unique=True, null=False)
    password = models.CharField(verbose_name='密码', max_length=32, null=False)
    avatar = models.ImageField(verbose_name='头像', upload_to='avatars/', blank=True, null=True)
    name = models.CharField(verbose_name='姓名', null=True, max_length=100)
    phone = models.CharField(verbose_name='用户电话', max_length=20)
    email = models.EmailField(verbose_name='用户邮箱')
    card = models.CharField(verbose_name='身份证', null=True, max_length=30)
    age = models.IntegerField(verbose_name='年龄', null=True)
    address = models.CharField(verbose_name='居住地址', max_length=200, null=True)
    gender = models.CharField(verbose_name='性别', null=True, max_length=10)
    nation = models.CharField(verbose_name='民族', null=True, max_length=200)


    def __str__(self):
        return "医生昵称：%s" % (self.username)

    class Meta:
        db_table = 'doctor_profile'
        verbose_name = '医生信息'
        verbose_name_plural = '医生信息'

# Create your models here.
