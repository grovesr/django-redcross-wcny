from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from redcross_wcny import urls
from redcross_wcny.views import handler400, handler404, handler500
import logging

logging.disable(logging.CRITICAL)

class PageNotFoundViewTests(TestCase):
    '''
    check page_not_found view
    '''
    def setUp(self):
        # Most ims_tests need access to the request factory and/or a user.
        self.factory = RequestFactory()
        
    def test_page_not_found_view(self):
        print 'running PageNotFoundViewTests.test_page_not_found_view... '
        self.assertTrue(urls.handler500.endswith('.handler500'))
        request = self.factory.get('/')
        response = handler404(request)
        self.assertEqual(response.status_code, 404)
        self.assertIn('Oops! It looks like you might be lost.',
                      response.content,
                    'page_not_found view didn''t generate the correct message when presented with an invalid URL')
    
class SuspiciousOperationViewTests(TestCase):
    '''
    Check suspicious_operation view
    '''
    def setUp(self):
        # Most ims_tests need access to the request factory and/or a user.
        self.factory = RequestFactory()
        
    def test_suspicious_operation_view(self):
        print 'running SuspiciousOperationViewTests.test_suspicious_operation_view... '
        self.assertTrue(urls.handler400.endswith('.handler400'))
        request = self.factory.get('/')
        response = handler400(request)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Hmm! There was something suspicious about that last request',
                      response.content,
                    'suspicuous operation view didn''t generate the correct message when presented with a suspicious request')
    
class ServerErrorViewTests(TestCase):
    '''
    check server_error view
    '''
    def setUp(self):
        # Most ims_tests need access to the request factory and/or a user.
        self.factory = RequestFactory()
        
    def test_server_error_view(self):
        print 'running ServerErrorViewTests.test_server_error_view... '
        self.assertTrue(urls.handler500.endswith('.handler500'))
        request = self.factory.get('/')
        response = handler500(request)
        self.assertEqual(response.status_code, 500)
        self.assertIn('Uh oh! It looks like there was some kind of server error!',
                      response.content,
                      'server_error view didn''t generate the correct message when presented with an Exception')