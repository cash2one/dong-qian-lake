# coding=UTF-8
from django.db import models

# Create your models here.
class Project(models.Model):
    area = models.CharField(u'区块分类',max_length=30)
    invest_subject = models.CharField(u'投资主体',max_length=30)
    project_schedule = models.CharField(u'项目进度',max_length=30)
    no = models.IntegerField()
    project_name = models.CharField(u'项目名称',max_length=100)
    project_type = models.CharField(u'项目类型',max_length=30,blank=True)
    
    total_invest     = models.BigIntegerField(u'总投资',default=0)
    planed_invest    = models.BigIntegerField(u'2012年计划建设投资',blank=True,default=0)
    completed_invest = models.BigIntegerField(u'2012年已完成投资',blank=True,default=0)

    funds_source = models.CharField(u'资金来源',max_length=30,blank=True)
    start_time = models.CharField(u'开工时间',max_length=100,blank=True)
    completed_time = models.CharField(u'竣工时间',max_length=100,blank=True)
    leader = models.CharField(u'牵头委领导',max_length=50)
    build_unit = models.CharField(u'建设单位或牵头单位',max_length=100,blank=True)
    project_information = models.TextField(u'项目推进情况',blank=True)
    problem = models.TextField(u'存在问题',blank=True)
    remark = models.TextField(u'备注',blank=True)
    
    photo = models.FileField(u'图片',upload_to='dong-qian-lake',blank=True,null=True)

    class Meta:
        verbose_name=u'项目'
        verbose_name_plural=u'项目'

    def __unicode__(self):
        return self.project_name


