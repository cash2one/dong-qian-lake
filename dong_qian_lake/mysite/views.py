# coding=UTF-8
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Project
from django.template import Context,RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime

def project_search_view(request):
    page = request.GET.get('page','1') 
    name = request.GET.get('project_name','')
    schedule = request.GET.get('project_schedule','')
    date_from = request.GET.get('date_from','')
    date_to = request.GET.get('date_to','')
    
    query_list = Project.objects.all()
    
    if name:
        query_list = query_list.filter(project_name__contains=name)
        print 20, query_list 

    if schedule:
        query_list = query_list.filter(project_schedule__contains=schedule)

    if date_from:
        query_list = query_list.filter(start_time__contains=date_from)

    if date_to:
        query_list = query_list.filter(completed_time__contains=date_to)
    
    paginator = Paginator(query_list,20)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    year = datetime.now().year
    
    year_list = []
    for i in range(year,1999,-1):
        year_list.append(i)

    url = request.get_full_path()

    return my_render_to_response(request,'search.html',{'query_list':projects,'year_list':year_list,'url':url})

def my_render_to_response(request,template,data_dict={}):
    return render_to_response(template,data_dict,context_instance=RequestContext(request))

def project_detail_view(request):
    id=request.GET.get('id','')
    project = Project.objects.get(pk=id)
    return my_render_to_response(request,'detail.html',{'project':project})
