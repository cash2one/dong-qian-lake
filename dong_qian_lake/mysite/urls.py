from django.conf.urls import patterns
from views import *

urlpatterns = patterns(
        '',
        (r'^accounts/login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
        (r'^accounts/logout/$',logout_view),
        (r'^search$',project_search_view),
        (r'^project$',project_detail_view),
        )
