from django.conf.urls import patterns
from views import *

urlpatterns = patterns(
        '',
        (r'^accounts/login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
        (r'^accounts/logout/$',logout_view),
        
        (r'^search$',search_view),
        
        (r'^project$',detail_view),

        (r'^progress/new$',add_progress_view),
        (r'^progress/list$',list_progress_view),
        (r'^progress/edit/(?P<id>\d+)/$',edit_progress_view),
        (r'^progress/delete/(?P<id>\d+)/$',delete_progress_view),

        (r'^overviews/new$',add_overview_view),
        (r'^overviews/edit/(?P<id>\d+)/$',edit_overview_view),
        (r'^overviews/delete/(?P<id>\d+)/$',delete_overview_view),
        


        (r'^test$',test_view),
        )
