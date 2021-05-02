from django.db import models
from django_resized import ResizedImageField

# Create your models here.
#index page
class IndexTitle(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

class TotalImages(models.Model):
    CATEGORY = (
        ("wedding", "wedding"),
        ("modelling", "modelling"),
        ("products", "products"),
        ("wildlife", "wildlife"),
        ("events", "events")
    )
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=15)
    image = ResizedImageField(size=[1000, 1000], quality=99)
    image_category = models.CharField(max_length=50, choices=CATEGORY, default='')
    
    

    def __str__(self):
        return self.title

class IndexServices(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class IndexServiceType(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    title_2 = models.CharField(max_length=30, default='')
    description_2 = models.TextField(default='')
    title_3 = models.CharField(max_length=30, default='')
    description_3 = models.TextField(default='')

    def __str__(self):
        return self.title

class IndexNumber(models.Model):
    title = models.CharField(max_length=30)
    number = models.IntegerField()

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    profile_pic = ResizedImageField(size=[1000, 1000], quality=99)
    name = models.CharField(max_length=50)
    about = models.TextField()
    twitter_link = models.CharField(max_length=300, null=True, blank=True)
    facebook_link = models.CharField(max_length=300, null=True, blank=True)
    insta_link = models.CharField(max_length=300, null=True, blank=True)
    youtube_link = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

class Address(models.Model):
   address = models.CharField(max_length=600)
   phone = models.CharField(max_length=20)
   email = models.CharField(max_length=100)
   
   def __str__(self):
        return self.phone

class CustomerOrder(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

class Videos(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    video = models.FileField()

    def __str__(self):
        return self.title
    






    