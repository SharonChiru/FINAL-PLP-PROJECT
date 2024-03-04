from django.db import models

from django.contrib.auth.models import User
 
class Category(models.Model):
    name=models.CharField(max_length=200)

    class Meta:
        ordering=['-name']
    
    def __str__(self):
        return self.name
    
class Vendor(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    vendor=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    location=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image')
    image_1=models.ImageField(blank=True,null=True,upload_to='image')
    image_2=models.ImageField(blank=True,null=True,upload_to='image')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=["-title"]

    def __str__(self):
        return self.title
    

    

