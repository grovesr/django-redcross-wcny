from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from . import views

handler400 = 'redcross_wcny.views.handler400'
handler404 = 'redcross_wcny.views.handler404'
handler500 = 'redcross_wcny.views.handler500'

urlpatterns = [
    # Examples:
    # url(r'^$', 'redcross.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url('^login/$', views.login,
         {'template_name':'registration/login.html'}, 
         name='login'),
    url('^logout/$', views.logout),
    url('^password_change/$', views.password_change,
        {'template_name':'registration/password_change.html'}, 
        name='password_change'),
    url('^password_change/done/$', views.password_change_done,
        {'template_name':'registration/password_change_done.html'}, 
        name='password_change_done'),
    url('^password_reset/$',  views.password_reset,
        {'template_name':'registration/password_reset.html'},
        name='password_reset'),
    url('^password_reset/done/$', views.password_reset_done,
        {'template_name':'registration/password_reset_done.html'}, 
        name='password_reset_done'),
    url('^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, 
        {'template_name':'registration/password_reset_confirm.html'}, 
        name='password_reset_confirm'),
    url('^reset/done/$', views.password_reset_complete,
        {'template_name':'registration/password_reset_complete.html'}, 
        name='password_reset_complete'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ims/$',views.home,name='home'),
    url(r'^ims/',include('ims.urls',namespace='ims')),
    url(r'^$', views.home,name='home'),
    url(r'^redcross_help$',views.redcross_help, name='redcross_help')
]

# serve uploaded media in development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
