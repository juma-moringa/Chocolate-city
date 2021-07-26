from django.test import TestCase
from .models import  Business, Neighbourhood, Profile  
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User(username="juma.a", password="pass123")
        self.user.save()
        self.neighbourhood= Neighbourhood(hood_name = "route4", hood_location= "Eastside", admin = self.user,hood_description='mtaa yetu')
        self.neighbourhood.save()
        self.profile = Profile(bio='my hood',email='email@g.com', id_number=3677093,user = self.user, neighbourhood = self.neighbourhood)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)
    
    def test_get_profile(self):
        self.profile.save_profile()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)
    
  
    def test_delete_method(self):
        self.profile.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)

class NeighbourhoodTestClass(TestCase):
    #Set up Method
    def setUp(self):
        '''
        test case for profiles
        '''
        self.user = User(username='juma')
        self.user.save()
        self.neighbourhood= Neighbourhood(hood_name = "route4", hood_location= "Eastside", admin = self.user,hood_description='mtaa yetu')
        self.neighbourhood.create_neighbourhood()

    def tearDown(self):
        Neighbourhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

    def test_create_neighborhood(self):
        self.neighbourhood.create_neighbourhood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_hood(self):
        self.neighbourhood.create_neighbourhood()
        self.neighbourhood.delete_hood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) == 0)

class BusinessTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User(username="juma", password="pass123")
        self.user.save()
        self.neighbourhood = Neighbourhood(hood_name="route4", hood_location="Eastside", admin=self.user, hood_description='mtaa yetuu')
        self.neighbourhood.save()
        self.business = Business(name='my hood', business_email='testemail@g.com',description='testcase business', neighbourhood_id=self.neighbourhood)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

      