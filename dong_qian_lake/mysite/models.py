from django.db import models

# Create your models here.
class Project(models.Model):
    area = models.CharField(max_length=30)
    invest_subject = models.CharField(max_length=30)
    project_schedule = models.CharField(max_length=30)
    no = models.IntegerField()
    project_name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=30,blank=True)
    
    total_invest     = models.BigIntegerField(default=0)
    planed_invest    = models.BigIntegerField(blank=True,default=0)
    completed_invest = models.BigIntegerField(blank=True,default=0)

    funds_source = models.CharField(max_length=30,blank=True)
    start_time = models.CharField(max_length=100,blank=True)
    completed_time = models.CharField(max_length=100,blank=True)
    leader = models.CharField(max_length=50)
    build_unit = models.CharField(max_length=100,blank=True)
    project_information = models.TextField(blank=True)
    problem = models.TextField(blank=True)
    remark = models.TextField(blank=True)

    def __unicode__(self):
        return self.project_name


