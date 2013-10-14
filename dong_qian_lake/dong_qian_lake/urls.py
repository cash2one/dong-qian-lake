from django.conf.urls import patterns, include, url
from settings import STATIC_ROOT,MEDIA_ROOT
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dong_qian_lake.views.home', name='home'),
<<<<<<< HEAD
     url(r'', include('mysite.urls')),
=======
     url(r'^v1/', include('src.v1.urls')),
>>>>>>> 5400b1aa6549329f63dc4ecc4ed09b331f2f7ba4
     url(r'^v2/', include('src.v2.urls')),
     url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':STATIC_ROOT}),
     url(r'^d-media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':MEDIA_ROOT}),

    # Uncomment the admin/doc line below to enable admin documentation:
#     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
