from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.conf import settings
try:
    adminName = settings.SITE_ADMIN[0]
except AttributeError:
    adminName=''
try:
    adminEmail = settings.SITE_ADMIN[1]
except AttributeError:
    adminEmail=''
try:
    siteVersion = settings.SITE_VERSION
except AttributeError:
    siteVersion=''
try:
    imsVersion = settings.IMS_VERSION
except AttributeError:
    imsVersion=''
def home(request):
    return render(request,'base/base.html',{'nav_home':1,
                                            'adminName':adminName,
                                            'adminEmail':adminEmail,
                                            'siteVersion':siteVersion,
                                            'imsVersion':imsVersion,})

def redcross_help(request):
    return render(request,'base/redcross_help.html',{'nav_help':1,
                                            'adminName':adminName,
                                            'adminEmail':adminEmail,
                                            'siteVersion':siteVersion,
                                            'imsVersion':imsVersion,})

def handler404(request):
    warningMessage = '''Oops! It looks like you might be lost.<br />
                    The requested page<br />
                    <span id="url-text">"%s"</span><br />
                    doesn't exist on this site.<br />
                    The site admin has been informed of the problem.<br />
                    Try one of these links to find what you're looking for<br />
                    ''' % request.build_absolute_uri()
    response = render_to_response('404.html', {'warningMessage':warningMessage},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
 
def handler500(request):
    errorMessage = '''Uh oh! It looks like there was some kind of server error!<br />
    Sorry about that.<br />
    The site admin has been informed of the problem.<br /><br />
    Please use the menu bar at the top to continue using the site.'''
    response = render_to_response('500.html',{'errorMessage':errorMessage},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
 
def handler400(request):
    errorMessage = '''Hmm! There was something suspicious about that last request.<br />
    Please try again.<br />
    The site admin has been informed of the problem.<br /><br />
    Please use the menu bar at the top to continue using the site.'''
    response = render_to_response('400.html', {'errorMessage':errorMessage},
                                  context_instance=RequestContext(request))
    response.status_code = 400
    return response