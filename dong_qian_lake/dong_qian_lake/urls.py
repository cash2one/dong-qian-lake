from django.conf.urls import patterns, include, url
from settings import STATIC_ROOT,MEDIA_ROOT
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dong_qian_lake.views.home', name='home'),
     url(r'', include('mysite.urls')),
     url(r'^static/(<?Ppath>.*)$', 'django.views.static.serve',{'document_root':MEDIA_ROOT}),

    # Uncomment the admin/doc line below to enable admin documentation:
#     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
