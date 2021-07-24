from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=100,blank=False)
    neighbourhood_location = models.CharField(max_length=100, blank=False)
    occupants_count = models.IntegerField()
    admin = models.ForeignKey(User,related_name='Hadmin', null=True,on_delete=models.CASCADE)

  
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='0')
    bio = models.TextField()  
    neighbourhood_id = models.ForeignKey(Neighbourhood, 
    related_name='members', 
    on_delete=models.CASCADE, 
    blank=True, null=True)
    neighbourhood_name = models.CharField(max_length=60,blank=False)
    location = models.CharField(max_length=60,blank=False)
      

class Business(models.Model): 
    business_name= models.CharField(max_length=100, blank=False) 
    user= models.ForeignKey(Profile,related_name='business_owner',on_delete=models.CASCADE,)   
    neighbourhood_id= models.ForeignKey(Neighbourhood,related_name='business',on_delete=models.CASCADE)
    business_email = models.CharField(max_length=50,blank=False)