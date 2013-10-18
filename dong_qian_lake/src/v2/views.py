# coding=UTF-8
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from models import ProjectOverView,ProjectProgress 
from django.template import Context,RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login
from django.forms import ModelForm
from django import forms
from dig_paginator import DiggPaginator
import urllib

class OverViewForm(ModelForm):
    
    class Meta:
        model = ProjectOverView

    def __init__(self,*args,**kwargs):
        super(OverViewForm,self).__init__(*args,**kwargs)
        for k,v in self.fields.items():
            v.widget.attrs.update({'class':'form-control'})

class ProgressForm(ModelForm):
    
    def __init__(self,*args,**kwargs):
        super(ProgressForm,self).__init__(*args,**kwargs)
        for k,v in self.fields.items():
            v.widget.attrs.update({'class':'form-control'})
            if k == 'problem' or k=='remark':
                v.widget.attrs.update({'rows':'3'})
            if k == 'project':
                v.widget.attrs.update({'class':'form-control selectpicker span3','data-live-search':'true'})

    class Meta:
        model = ProjectProgress

@login_required
def add_progress_view(request):
    f = ProgressForm()

    if request.POST:
        f = ProgressForm(request.POST,request.FILES)
        if f.is_valid():
            f.save()
            return redirect(search_view)

    return manage_render_to_response(request,'new_progress.html',{'form':f})

@login_required
def edit_progress_view(request,id):
    p = ProjectProgress.objects.get(pk=id)
    f = ProgressForm(instance=p)

    if request.POST:
        f = ProgressForm(request.POST,request.FILES,instance=p)
        if f.is_valid():
            f.save()
            return redirect(search_view)
    return manage_render_to_response(request,'edit_progress.html',{'form':f,'id':id})

@login_required
def delete_progress_view(request,id):
    p = ProjectProgress.objects.get(pk=id)
    p.delete()
    return redirect(search_view)

@login_required
def add_overview_view(request):
    f = OverViewForm()

    if request.POST:
        f = OverViewForm(request.POST)

        if f.is_valid():
            f.save()
            return redirect(search_view)
    return manage_render_to_response(request,'new_overview.html',{'form':f})

@login_required
def edit_overview_view(request,id):
    o = ProjectOverView.objects.get(pk=id)
    f = OverViewForm(instance=o)

    if request.POST:
        f = OverViewForm(request.POST,instance=o)
        if f.is_valid():
            f.save()
            return redirect(search_view)
    return manage_render_to_response(request,'edit_overview.html',{'form':f,'id':id})

@login_required
def delete_overview_view(request,id):
    o  = ProjectOverView.objects.get(pk=id)
    o.delete()
    return redirect(search_view)

def test_view(request):
    return my_render_to_response(request,'test.html')

def logout_view(request):
    logout(request)
    return redirect(search_view)

@login_required
def search_view(request):
    page = request.GET.get('page','1') 
    name = request.GET.get('project_name','')
    schedule = request.GET.get('project_schedule','')
    date_from = request.GET.get('date_from','')
    date_to = request.GET.get('date_to','')
    invest_subject = request.GET.get('invest_subject','') 

    query_list = ProjectOverView.objects.all()
    
    if name:
        query_list = query_list.filter(project_name__contains=name)

    if schedule:
        query_list = query_list.filter(project_schedule__contains=schedule)

    if date_from:
        query_list = query_list.filter(start_time__contains=date_from)

    if date_to:
        query_list = query_list.filter(completed_time__contains=date_to)

    if invest_subject:
        query_list = query_list.filter(invest_subject__contains=invest_subject)
    
    paginator = DiggPaginator(query_list,10,body=5,padding=2)
    
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    year = datetime.now().year + 10
    
    year_list = []
    for i in range(year,1999,-1):
        year_list.append(i)

    query_dict = request.GET.dict()

    for k,v in query_dict.items():
        if k == 'page':
            query_dict.pop('page')

    query_string = urllib.urlencode(query_dict)

    user = request.user
    return my_render_to_response(request,'search.html',{'query_list':projects,'year_list':year_list,'query_string':query_string,'user':user})

def my_render_to_response(request,template,data_dict={}):
    return render_to_response(template,data_dict,context_instance=RequestContext(request))

def manage_render_to_response(request,template,data_dict={}):
    if request.user.is_staff:
        return my_render_to_response(request,template,data_dict)
    else:
        return redirect(search_view)

@login_required
def detail_view(request):
    id=request.GET.get('id','')
    
#    if request.user.is_staff:
#        pass
#    else:
    overview = ProjectOverView.objects.get(pk=id)
    
    progress_list = ProjectProgress.objects.filter(project=overview)

    return my_render_to_response(request,'detail.html',{'project':overview,'progress_list':progress_list})

@login_required
def list_progress_view(request):
    foreign_key = request.GET.get('foreignkey','')
    page = request.GET.get('page','')
    query_list = ProjectProgress.objects.all()
    
    if foreign_key:
        p = ProjectOverView.objects.get(pk=foreign_key)
        query_list = query_list.filter(project=p)

    paginator = DiggPaginator(query_list,10,body=5,padding=2)

    try:
        query_list = paginator.page(page)
    except PageNotAnInteger:
        query_list = paginator.page(1)
    except EmptyPage:
        query_list = paginator.page(paginator.num_pages)

    query_dict = request.GET.dict()

    for k,v in query_dict.items():
        if k == 'page':
            query_dict.pop('page')

    query_string = urllib.urlencode(query_dict)

    return manage_render_to_response(request,'list_progress.html',{'query_list':query_list,'query_string':query_string,'overview':p})

@login_required
def flow_view(request):
    error_msg = '' 
    if request.POST:
        if request.POST.get('is_current',''):
            data_dict = request.POST.dict()
            return manage_render_to_response(request,'screenshot_flow.html',{'data':data_dict}) 
        else:
            error_msg = u'请选择一条纪录以表示当前进度。'
    return manage_render_to_response(request,'flow.html',{'error':error_msg})

