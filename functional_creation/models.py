

from django.db import models
# from sympy import false

from account.models import User

# Create your models here.

class discription(models.Model):
    discription = models.TextField(max_length=200, blank=False)
    class Meta:
        abstract = True
class creation_post(discription):
  
   SELECT = 'select'
   FASHION ='Fashion'
   JEWELLERY = 'Jewellery'
   TOYS = 'Toys'
   INTERIOR ='Interior/Set Design'
   GRAPHICS = 'Graphics'
   
   STATUS = [
        (SELECT, ('---select Design ---')),
        (FASHION, ('Fashion')),
        (JEWELLERY, ('Jewellery')),
        (TOYS, ('Toys')),
        (INTERIOR, ('Interior/Set Design')),
        (GRAPHICS, ('Graphics')),
       
   ]
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   type = models.CharField( max_length=32, choices=STATUS, default=SELECT, blank=False)
   image = models.ImageField(upload_to='heriage/', null=True, blank=True)
   create_date = models.DateTimeField( auto_now_add=True, blank=True)


class auth_creation(models.Model):
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
#    profile = models.ImageField(upload_to='avatars/', null=True, blank=True)
   document = models.FileField(upload_to='documents/', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)


# festion
class fepost(discription):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='function/de', null=True, blank=True)



class authfe(models.Model):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/cre/fun/de', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)


   
# toy
class jewpost(discription):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='function/gew', null=True, blank=True)



class authjew(models.Model):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/cre/fun/gew', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

   
# toy
class toypost(discription):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='function/toy', null=True, blank=True)



class authtoy(models.Model):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/cre/fun/toy', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# set design

class set_designpost(discription):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='function/set', null=True, blank=True)

class authset_design(models.Model):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/cre/fun/set', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# gra

class graphic_post(discription):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='function/graphic', null=True, blank=True)

class auth_graphic(models.Model):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/cre/fun/graphic', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)


# archecture
class architecture_post(discription):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='function/arch', null=True, blank=True)

class auth_architecture(models.Model):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/cre/fun/arch', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# advertising
class advertising_post(discription):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='function/ad', null=True, blank=True)
class auth_advertising(models.Model):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/cre/fun/ad', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# creative R&D

class creative_research_and_development_post(discription):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='function/ad', null=True, blank=True)

class auth_creative_research_and_development(models.Model):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/cre/fun/ad', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# creative event service

class creative_event_service_post(discription):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='function/ser', null=True, blank=True)

class auth_creative_event_service(models.Model):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/cre/fun/ser', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# digital services

class digital_service_post(discription):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='function/ser', null=True, blank=True)

class auth_digital_creative(models.Model):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/cre/fun/ser', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

