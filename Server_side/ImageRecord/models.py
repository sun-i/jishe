from django.db import models


class ImageRecord(models.Model):
    id = models.AutoField(primary_key=True)
    attribute = models.IntegerField(verbose_name='属性', null=True)
    attributeText = models.CharField(verbose_name='属性名称', max_length=100, null=True)
    imageUserName = models.CharField(verbose_name='上传用户', max_length=100, null=False)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    imagePath = models.CharField(verbose_name='图片路径', max_length=100, null=True)
    imageUrl = models.CharField(verbose_name='图片URL', max_length=100, null=True)
    imageName = models.CharField(verbose_name='图片名称', max_length=100, null=True)

    def __str__(self):
        return "记录名称: %s" % (self.imageName)

    class Meta:
        db_table = 'image_record'
        verbose_name = '图片记录'
        verbose_name_plural = '图片记录'
