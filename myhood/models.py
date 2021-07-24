from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField
# Create your models here.

# 1. myhood class
class Neighbourhood(models.Model):
    hood_picture= CloudinaryField('image')
    neighbourhood_name = models.CharField(max_length=100,blank=False)
    neighbourhood_location = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    occupants_count = models.IntegerField()
    admin = models.ForeignKey(User,related_name='Hood_admin', null=True,on_delete=models.CASCADE)

    #neighbourbood methods
    def __str__(self):
         return self.neighbourhood_name

    def create_neighbourhood(self):
        self.save() 

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    # def find_neighbourhood(cls, neighbourhood_id):
    #     return cls.objects.filter(id=neighbourhood_id) 
    def find_neighbourhood(cls,search_term):
        myhood = cls.objects.filter(name__icontains = search_term)
        return myhood

    def update_neighborhood(self):
        neighbourhood_name = self.name
        self.name = neighbourhood_name  
        
    @classmethod
    def update_occupants(cls,neighbourhood_id):
        member = cls.objects.get(id=neighbourhood_id)
        new_count = member.occupants_count + 1
        cls.objects.filter(id = neighbourhood_id).update(occupants_count = new_count) 


# 2. Userprofile
class Profile(models.Model):
    profile_picture= CloudinaryField('image', default='default.png')
    user = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE)
    bio = models.TextField()  
    neighbourhood_id = models.ForeignKey(Neighbourhood, 
    related_name='hood_members', 
    on_delete=models.CASCADE, 
    blank=True, null=True)
    neighbourhood_name = models.CharField(max_length=60,blank=False)
    location = models.CharField(max_length=60,blank=False)

    # profile methods
    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()  

# 3. Business class
class Business(models.Model): 
    business_name= models.CharField(max_length=100, blank=False) 
    user= models.ForeignKey(Profile,related_name='business_owner',on_delete=models.CASCADE,)   
    neighbourhood_id= models.ForeignKey(Neighbourhood,related_name='business',on_delete=models.CASCADE)
    business_email = models.CharField(max_length=50,blank=False)

    # profile methods
    def __str__(self):
        return self.business_name

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

    def update_business(self):
        business_name = self.name
        self.name = business_name     


class Post(models.Model):
    title = models.CharField(max_length=60, null=True)
    post = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='postowner')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='hood_post')
   

    def __str__(self):
        return f'{self.title} Post'    
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()        