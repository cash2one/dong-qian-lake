# coding=UTF-8
from django.db import models
from datetime import datetime

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

class ProjectOverView(models.Model):
    project_name = models.CharField(u'项目名称',max_length=100)
    project_schedule = models.CharField(u'项目进度',max_length=30)
    invest_subject = models.CharField(u'投资主体',max_length=30)
    start_time = models.CharField(u'开工时间',max_length=100,blank=True)
    completed_time = models.CharField(u'竣工时间',max_length=100,blank=True)

    project_content = models.CharField(u'"十二五"实施内容',max_length=100,blank=True)
    year_limit = models.CharField(u'实施年限',max_length=20,blank=True)
    planed_invest = models.CharField(u'"十二五"计划总投资',max_length=20,blank=True)
    year_content = models.CharField(u'2012实施内容',max_length=100,blank=True)
    response_for = models.CharField(u'责任部门',max_length=50,blank=True)

    def __unicode__(self):
        return self.project_name

    class Meta:
        verbose_name = u'项目概况'
        verbose_name_plural = u'项目概况'


class ProjectProgress(models.Model):

    def get_year_list():
        year = datetime.now().year
        year_list = []
        for i in range(year,1999,-1):
            year_list.append((str(i),str(i)))
        return year_list

    def get_month_list():
        month_list = []
        for i in range(1,13):
            month_list.append((str(i),str(i)))
        return month_list
    YEAR_LIST = get_year_list()
    CURRENT_YEAR = str(datetime.now().year)
    MONTH_LIST = get_month_list() 

    name = models.CharField(u'名称',max_length=100)
    year = models.CharField(u'年度',choices=YEAR_LIST,default=CURRENT_YEAR,max_length=10)
    month = models.CharField(u'月份',choices=MONTH_LIST,default='1',max_length=2)
    invest= models.CharField(u'投资额（万元）',max_length=30)
    progress = models.CharField(u'目前进度',max_length=30)
    problem = models.TextField(u'存在问题',blank=True)
    remark = models.TextField(u'备注',blank=True)
    photo = models.FileField(u'图片',upload_to='dong-qian-lake-progress',blank=True,null=True)
    responsible_for = models.CharField(u'责任部门',max_length=50)
    
    project = models.ForeignKey(ProjectOverView,verbose_name=u'项目概况')

    def __unicode__(self):
        return u'%s %s年 %s月' % (self.name,self.year,self.month)

    class Meta:
        verbose_name = u'项目进度'
        verbose_name_plural = u'项目进度'


