# Generated by Django 4.1.7 on 2023-04-15 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('recordId', models.IntegerField(null=True, verbose_name='挂号记录ID')),
                ('patientId', models.IntegerField(null=True, verbose_name='患者ID')),
                ('doctorId', models.IntegerField(null=True, verbose_name='医生ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('clinic', models.CharField(default='心脏科室', max_length=200, null=True, verbose_name='科室')),
                ('chief_complaint', models.TextField(null=True, verbose_name='主诉')),
                ('medical_history', models.TextField(null=True, verbose_name='既往病史')),
                ('proposals', models.TextField(null=True, verbose_name='医嘱')),
                ('diagnosis_result', models.TextField(null=True, verbose_name='诊断结果')),
            ],
            options={
                'verbose_name': '医嘱信息',
                'verbose_name_plural': '医嘱信息',
                'db_table': 'medic_record',
            },
        ),
    ]
