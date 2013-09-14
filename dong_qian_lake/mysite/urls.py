from django.conf.urls import patterns
from views import *

urlpatterns = patterns(
        '',
        (r'^search$',project_search_view),
        (r'^project$',project_detail_view),
        )
