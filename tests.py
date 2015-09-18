from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from redcross_wcny import urls
from views import handler404, handler500


class PageNotFoundViewTests(TestCase):
    '''
    check page_not_found view
    '''
    
    def test_page_not_found_view(self):
        print 'running PageNotFoundViewTests.test_page_not_found_view... '
        self.assertTrue(urls.handler500.endswith('.handler500'))
        request = self.client.get('/')
        response = handler404(request)
        self.assertEqual(response.status_code, 404)
        self.assertIn('Oops! It looks like you might be lost.',
                      response.content,
                    'page_not_found view didn''t generate the correct message when presented with an invalid URL')
    
class ServerErrorViewTests(TestCase):
    '''
    check server_error view
    '''
    def setUp(self):
        # Most ims_tests need access to the request factory and/or a user.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testUser', password='12345678')
        
    def test_server_error_view(self):
        print 'running ServerErrorViewTests.test_server_error_view... '
        self.assertTrue(urls.handler500.endswith('.handler500'))
        request = self.client.get('/')
        response = handler500(request)
        self.assertEqual(response.status_code, 500)
        self.assertIn('Uh oh! It looks like there was some kind of server error!',
                      response.content,
                      'server_error view didn''t generate the correct message when presented with an Exception')