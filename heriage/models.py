from django.db import models
# from sympy import false

from account.models import User
from app.models import artist_profile

# Create your models here.

class discription(models.Model):
    discription = models.TextField(max_length=200, blank=False)
    class Meta:
        abstract = True
class heriage_post(discription):

   SELECT = 'select'
   ARTCRAFTS ='Art Crafts'
   FESTIVALS = 'Festivals'
   CELEBRATION = 'Celebration'
   
   STATUS = [
       (SELECT, ('---select Types---')),
       (ARTCRAFTS,('Art Crafts')),
       (FESTIVALS,('Festivals')),
       (CELEBRATION,('Celebration')),
   ]
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   type = models.CharField( max_length=32, choices=STATUS, default=SELECT, blank=False)
   image = models.ImageField(upload_to='heriage/')
   create_date = models.DateTimeField( auto_now_add=True, blank=True)



class authHeritage(models.Model):
#    skills
   SELECT = 'select'
   ARTIST ='Artist'
   
   
   STATUS5 = [
       (SELECT, ('---select skills---')),
       (ARTIST,('Artist'))
       
        
   ]
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   skills = models.CharField( max_length=32, choices=STATUS5, default=SELECT, blank=True)
   document = models.FileField(upload_to='documents/', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)


# arts craft

class arts_craft_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   name= models.ForeignKey(artist_profile, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='heriage/craft')
   create_date = models.DateTimeField( auto_now_add=True, blank=True)



class autharts(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/arts and crafts', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# festival

class festival_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='heriage/festival')
   create_date = models.DateTimeField( auto_now_add=True, blank=True)

class authfestival(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/festival', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# celebrations

class cele_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='heriage/cele')
   create_date = models.DateTimeField( auto_now_add=True, blank=True)

class authceles(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/cele', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# is_historical

class historical_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='heriage/cele')
   create_date = models.DateTimeField( auto_now_add=True, blank=True)

class authhistorical(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/cele', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# museum

class museum_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='heriage/cele')
   create_date = models.DateTimeField( auto_now_add=True, blank=True)

class authmuseum(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/cele', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# labries 

class labrary_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='heriage/lab')
   create_date = models.DateTimeField( auto_now_add=True, blank=True)

class authlabrary(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/lab', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# archives

class arch_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='heriage/arch')
   create_date = models.DateTimeField( auto_now_add=True, blank=True)

class autharch(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/arch', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)


