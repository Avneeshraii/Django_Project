from django.db import models

class AddClient(models.Model):
    # Field for storing the details of the profile
    name= models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    phone = models.IntegerField(max_length=10)
    address = models.CharField(max_length=200)
    
    
# class AddUser(models.Model):
#     name= model.charfield(max_length=100)
    
    
    def __str__(self):
        return self.name 
    