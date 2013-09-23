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

class OverViewForm(ModelForm):
    
    class Meta:
        model = ProjectOverView

class ProgressForm(ModelForm):

    class Meta:
        model = ProjectProgress

def add_progress_view(request):
    f = ProgressForm()

    if request.POST:
        f = ProgressForm(request.POST,request.FILES)

        if f.is_valid():
            f.save()
            return redirect(search_view)

    return my_render_to_response(request,'new_progress.html',{'form':f})

def edit_progress_view(request,id):
    p = ProjectProgress.objects.get(pk=id)
    f = ProgressForm(instance=p)

    if request.POST:
        f = ProgressForm(request.POST,request.FILES,instance=a)
        if f.is_valid():
            f.save()
            return redirect(search_view)
    return my_render_to_response(request,'edit_progress.html',{'form':f})

def delete_progress_view(request,id):
    p = ProjectProgress.objects.get(pk=id)
    p.delete()
    return redirect(search_view)

def test_view(request):
    return my_render_to_response(request,'test.html')

def logout_view(request):
    logout(request)
    return redirect('/search')

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
        print 20, query_list 

    if schedule:
        query_list = query_list.filter(project_schedule__contains=schedule)

    if date_from:
        query_list = query_list.filter(start_time__contains=date_from)

    if date_to:
        query_list = query_list.filter(completed_time__contains=date_to)

    if invest_subject:
        query_list = query_list.filter(invest_subject__contains=invest_subject)
    
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

def detail_view(request):
    id=request.GET.get('id','')
    
#    if request.user.is_staff:
#        pass
#    else:
    overview = ProjectOverView.objects.get(pk=id)
    
    progress_list = ProjectProgress.objects.filter(project=overview)

    return my_render_to_response(request,'detail.html',{'project':overview,'progress_list':progress_list})


