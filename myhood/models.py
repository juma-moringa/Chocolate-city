from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

# 1. myhood class
class Neighbourhood(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE,related_name='admin')
    hood_photo = CloudinaryField('image', default='image')
    hood_name = models.CharField(max_length=60)
    hood_location = models.CharField(max_length=60)
    hood_description = models.TextField(max_length=150, blank=True)
    

    def __str__(self):
        return self.hood_name

    def create_neighbourhood(self):
        self.save()  

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def find_hood(cls, hood_id):
        return cls.objects.filter(id=hood_id)

    def update_hood(self):
        hood_name = self.hood_name
        self.hood_name = hood_name

# 2. Userprofile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.IntegerField(default=0)
    email = models.CharField(max_length=30, blank=True)
    profile_pic = CloudinaryField('profile')
    bio = models.TextField(max_length=500, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile
    
    

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(cls, id):
        Profile.objects.get(user_id=id)

# 3. Business class
class Business(models.Model): 
    name = models.CharField(max_length=100, blank=False) 
    user= models.ForeignKey(Profile,related_name='business_owner',on_delete=models.CASCADE,)   
    neighbourhood_id= models.ForeignKey(Neighbourhood,related_name='business',on_delete=models.CASCADE)
    business_email = models.CharField(max_length=50,blank=False)
    description = models.TextField(max_length=500, blank=True)

    # profile methods
    def __str__(self):
        return self.name

    def save_business(self):
        self.save()

    def create_business(self):
            self.save()

    def delete_business(self):
        self.delete()   

    @classmethod
    def find_business(cls,business_id):
        business = cls.objects.get(id = business_id)
        return business
    @classmethod
    def search_by_name(cls,search_term):
    	businesses = cls.objects.filter(name__icontains=search_term)
    	return businesses
  

# 4. post class
class Post(models.Model):
    title = models.CharField(max_length=60, null=True)
    post = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='postowner')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='hood_post')
   

   # post methods
    def __str__(self):
        return self.title    
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()        


