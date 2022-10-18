
from django.db import models
# from sympy import false

from account.models import User

# Create your models here.

class discription(models.Model):
    discription = models.TextField(max_length=200, blank=False)
    class Meta:
        abstract = True
class media_post(discription):



   SELECT = 'select'
   BOOKS ='Books'
   MAGAZINES = 'Magazines'
   COMICS = 'Comics'
   SCULPTURE ='Sculpture'
   POTTERY = 'Pottery'
   
   STATUS = [
        (SELECT, ('---select Publishing---')),
        (BOOKS, ('Books')),
        (MAGAZINES, ('Magazines')),
        (COMICS, ('Comics')),
        (SCULPTURE, ('Sculpture')),
        (POTTERY, ('Pottery')),
       
   ]
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   type = models.CharField( max_length=32, choices=STATUS, default=SELECT, blank=False)
   image = models.ImageField(upload_to='heriage/', null=True, blank=True)
   create_date = models.DateTimeField( auto_now_add=True, blank=True)


class auth_media(models.Model):
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

# bookes
class book_post(discription):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='media/book', null=True, blank=True)

class auth_book(models.Model):

   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/book', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# maga
class maga_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='media/maga', null=True, blank=True)

class maga_book(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/maga', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# maga
class com_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='media/com', null=True, blank=True)

class auth_com(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/com', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# fil
class fil_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='media/fil', null=True, blank=True)

class auth_fil(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/fil', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# tele
class tele_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='media/tele', null=True, blank=True)

class auth_tele(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/tele', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# rad
class rad_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='media/rad', null=True, blank=True)

class auth_rad(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/rad', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# musiv video
class music_video_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='media/music_video', null=True, blank=True)

class auth_music_video(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/music_video', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# digical content
class digital_content_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='media/digital_content', null=True, blank=True)

class auth_digital_content(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/digital_content', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# software
class software_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='media/software', null=True, blank=True)

class auth_software(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/software', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# video game
class video_game_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='media/video_game', null=True, blank=True)

class auth_video_game(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/video_game', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)

# animation
class animation_post(discription):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   title = models.CharField(max_length=100, blank=False)
   image = models.ImageField(upload_to='media/animation', null=True, blank=True)

class auth_animation(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   phone_no = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   document = models.FileField(upload_to='documents/animation', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)


