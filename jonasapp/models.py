from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    
    gender_options = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    
    last_name = models.CharField(max_length=30, null=True)
    first_name = models.CharField(max_length=30, null=True)
    middle_name = models.CharField(max_length=30, blank=True, default="N/A")
    age = models.PositiveBigIntegerField(null=True)
    gender = models.CharField(choices=gender_options, max_length=1)
    address = models.CharField(max_length=255, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.last_name
    
    
class Post(models.Model):
    PET_CHOICES = {
        ('dog', 'Dog'),
        ('cat', 'Cat'),
    }
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=255, null=True)
    image = models.ImageField(upload_to="post_image" ,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.CharField(choices=PET_CHOICES, max_length=80, default='dog')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
    
class Report(models.Model):
    location = models.CharField(max_length=255, null=True)   
    description = models.TextField(max_length=255, null=True)
    image = models.ImageField(upload_to="post_image" ,null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.location
    