from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from . import views

handler400 = 'ims_dev.views.handler400'
handler404 = 'ims_dev.views.handler404'
handler500 = 'ims_dev.views.handler500'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'redcross.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ims/',include('ims.urls',namespace='ims')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',name='logout'),
    url(r'^$', views.home,name='home'),
    url(r'^redcross_help$',views.redcross_help, name='redcross_help')
)

# serve uploaded media in development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
