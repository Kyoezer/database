from django.db import models

# Create your models here.
from django.db import models
# from sympy import false

from account.models import User

# Create your models here.

class discription(models.Model):
    discription = models.TextField(max_length=200, blank=False)
    class Meta:
        abstract = True
class art_post(discription):


   SELECT = 'select'
   PAINTINGS ='Paintings'
   DIGITAL_ART = 'Digital Art'
   PHOTOGRAPHY = 'Photography'
   SCULPTURE ='Sculpture'
   POTTERY = 'Pottery'
   
   STATUS = [
        (SELECT, ('---select Visual Arts---')),
        (PAINTINGS, ('Paintings')),
        (DIGITAL_ART, ( 'Digital Art')),
        (PHOTOGRAPHY, ('Photography')),
        (SCULPTURE, ('Sculpture')),
        (POTTERY, ('Pottery'))
       
   ]
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   type = models.CharField( max_length=32, choices=STATUS, default=SELECT, blank=False)
   image = models.ImageField(upload_to='heriage/', null=True, blank=True)
   create_date = models.DateTimeField( auto_now_add=True, blank=True)


class authart(models.Model):
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
   skills = models.CharField( max_length=32, choices=STATUS5, default=SELECT, blank=False)
   document = models.FileField(upload_to='documents/', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# painting

class paint_post(discription):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='arts/painting', null=True, blank=True)

class authpaint(models.Model):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/painting', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# digital arts

class digital_post(discription):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='arts/digital', null=True, blank=True)

class authdigital(models.Model):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/digital', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# photography

class photo_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='arts/photo', null=True, blank=True)

class authphoto(models.Model):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/photo', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# sculpture

class sulp_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='arts/scul', null=True, blank=True)

class authsulp(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/scul', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# pottery

class pot_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='arts/pot', null=True, blank=True)

class authpot(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/pot', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)


# livevideo
class live_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='arts/live', null=True, blank=True)

class authlive(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/live', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# theater
class the_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='arts/thea', null=True, blank=True)

class auththe(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/thea', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# dance
class dance_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='arts/dance', null=True, blank=True)

class authdance(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/dance', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# oprra

class opera_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='arts/opera', null=True, blank=True)

class authopera(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/opera', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)


# pupetry
class pup_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='arts/pup', null=True, blank=True)

class authpup(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/pup', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)