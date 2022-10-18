from django.db import models
from account.models import User

from event.models import addevent

# Create your models here.
class publiccontact(models.Model):
   event= models.ForeignKey(addevent, on_delete=models.CASCADE)
   email = models.EmailField( unique=True)
   first_name = models.CharField(('first name'), max_length=30,)
   last_name = models.CharField(('last name'), max_length=30,)
   phone = models.IntegerField()
   discription= models.TextField(max_length=300, blank=True)
   submit_date = models.DateTimeField( auto_now_add=True, blank=True)

   def __str__(self):
       return '%s - %s' % (self.first_name, self.event) 
   @property
   def title(self):
       return self.event.title

   @property
   def user(self):
       return self.event.user
       
class admincontact(models.Model):
   name = models.CharField(('full name'), max_length=30,)
   email = models.EmailField( unique=True)
   phone = models.IntegerField()
   discription= models.TextField(max_length=300, blank=True)
   submit_date = models.DateTimeField( auto_now_add=True, blank=True)

   def __str__(self):
       return (self.name)