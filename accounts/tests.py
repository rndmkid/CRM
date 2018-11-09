from django.test import TestCase
#from subscribers.models import Subscriber

# Create your tests here.

##class SubscriberTestCase(TestCase):
##    def setUp(self):
##        Subscriber.objects.create(username="test", password="xyz123bitch")
##
##    def test_exists(self):
##        testing = Subscriber.objects.get(username="test")
        
from django.contrib.auth.forms import AuthenticationForm

class AuthFormTestCase(TestCase):
##    def setUp(self):
##        form = AuthenticationForm(cleaned_data={'username': 'testUser',
##                                                'password': 'testPassword'})

    def test_get_data(self):
        form = AuthenticationForm(cleaned_data={'username': 'testUser',
                                                'password': 'testPassword'})
        self.assertEqual(form.cleaned_data.get('username'), 'testUser')
        self.assertEqual(form.cleaned_data.get('password'), 'testPassword')
        
