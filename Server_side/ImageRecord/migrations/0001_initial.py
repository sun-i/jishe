# Generated by Django 4.1.7 on 2023-04-15 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('attribute', models.IntegerField(null=True, verbose_name='属性')),
                ('attributeText', models.CharField(max_length=100, null=True, verbose_name='属性名称')),
                ('imageUserName', models.CharField(max_length=100, verbose_name='上传用户')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('imagePath', models.CharField(max_length=100, null=True, verbose_name='图片路径')),
                ('imageUrl', models.CharField(max_length=100, null=True, verbose_name='图片URL')),
                ('imageName', models.CharField(max_length=100, null=True, verbose_name='图片名称')),
            ],
            options={
                'verbose_name': '图片记录',
                'verbose_name_plural': '图片记录',
                'db_table': 'image_record',
            },
        ),
    ]
