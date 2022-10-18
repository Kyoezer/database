
from email.message import EmailMessage
from django.db import models
# from sympy import false
from django.db import models


from account.models import User

class IpModel(models.Model):
    ip = models.CharField(max_length=100)
    
class authUser(models.Model):

#    dzongkha

   SELECT = 'select'
   BUMTHANG='Bumthang'
   CHUKHA='Chukha'
   DAGANA='Dagana'
   GASA='Gasa'
   HAA = 'Haa'
   LHUNTSE='Lhuntse'
   MONGAR='Mongar'
   PARO = 'Paro'
   PAMAGATSHEL='Pemagatshel'
   PUNAKHA='Punakha'
   SAMDRUP_JONGKHAR='Samdrup Jongkhar '
   SAMTSE='Samtse'
   SARPANG='Sarpang'
   THIMPHU = 'Thimphu'
   TRASHIGANG = 'Trashigang'
   TRASHIYANGTSE='Trashiyangtse'
   TRONGSA='Trongsa'
   TSIRANG='Tsirang'
   WANGDUE='Wangdue Phodrang'
   ZHEMGANG='Zhemgang'
   
   
   STATUS2 = [
       (SELECT, ('---Select Dzongkhag---')),
       (BUMTHANG,('Bumthang')),
       (CHUKHA, ('Chukha')),
       (DAGANA, ('Dagana')),
       (GASA, ('Gasa')),
       (HAA , ('Haa')),
       (LHUNTSE, ('Lhuntse')),  
       (MONGAR, ('Mongar')),
       (PARO , ('Paro')),
       (PAMAGATSHEL, ('Pemagatshel')),
       (PUNAKHA, ('Punakha')),
       (SAMDRUP_JONGKHAR, ('Samdrup Jongkhar ')),
       (SAMTSE, ('Samtse')),
       (SARPANG, ('Sarpang')),
       (THIMPHU, ('Thimphu')),
       (TRASHIGANG, ('Trashigang')),
       (TRASHIYANGTSE, ('Trashiyangtse')),
       (TRONGSA, ('Trongsa')),
       (TSIRANG, ('Tsirang')),
       (WANGDUE, ('Wangdue Phodrang')),
       (ZHEMGANG, ('Zhemgang')),
       
       
   ]
# marital status
   SELECT = 'select'
   SINGLE = 'Single'
   MARRIED = 'Married'
   
   
   STATUS3 = [
       (SELECT, ('---Select Maritals---')),
       (SINGLE, ('Single')),
       (MARRIED, ('Married')),
       
   ]
#  Employment  
   SELECT = 'select'
   EMPLOYED = 'Employed'
   UNEMPLOYED = 'Unemployed'
   STUDENT = 'Student'
   BUSINESS = 'Business'
   
   
   STATUS4 = [
       (SELECT, ('---Select Employment---')),
       (EMPLOYED, ('Employed')),
       (UNEMPLOYED, ('Unemployed')),
       (STUDENT, ('Student')),
       (BUSINESS, ('Business')),
       
   ]
#    skills
 
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   cell_number = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   Dzongkhag = models.CharField( max_length=32, choices=STATUS2, default=SELECT,)
   marital_status = models.CharField( max_length=32, choices=STATUS3, default=SELECT,)
   employment_status = models.CharField( max_length=32, choices=STATUS4, default=SELECT,)
   document = models.FileField(upload_to='documents/', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)
   

class pubemail(models.Model):
    
    mail = models.EmailField(max_length= 100, unique=False)
    is_show_mail = models.BooleanField(('show'), default=True)
    # is_hide_mail = models.BooleanField(('hide'), default=False)
    
    class Meta:
        abstract = True

class pubphone(models.Model):
   
   phone = models.CharField( unique=False, max_length=8, null=True, blank=True,)
   is_show = models.BooleanField(('show'), default=True)
#    is_hide = models.BooleanField(('hide'), default=False)
   class Meta:
        abstract = True
class profiletype(models.Model):
   
# profile type
   SELECT = 'select'
   PERSONAL ='Personal'
   COMPANY = 'Company'
   ORGINIZATION = 'Orginization'
   GROUP = 'Group'
   
   
   STATUS8 = [
       (SELECT, ('Select')),
       (PERSONAL,('Personal')),
       (COMPANY, ('Company')),
       (ORGINIZATION,('Orginization')),
       (GROUP,('Group')),
           
   ]
   profile_type = models.CharField( max_length=32, choices=STATUS8, blank=True, default=SELECT)
   is_shows = models.BooleanField(('show'), default=True)
   class Meta:
        abstract = True

class genders(models.Model):
   #    gender
   SELECT = 'select'
   MALE ='Male'
   FEMALE= 'Female'
   OTHER = 'Others'
   
   
   STATUS7 = [
       (SELECT, ('Select')),
       (MALE,('Male')),
       (FEMALE,('Female')),
       (OTHER,('Other'))
           
   ]
   gender = models.CharField( max_length=32, choices=STATUS7, default=SELECT)
   is_showed = models.BooleanField(('show'), default=True)
   class Meta:
        abstract = True

class portfolio(models.Model):
   protfolio_image = models.FileField(upload_to='protfolio', null=True, blank=True)
   discription = models.TextField(max_length=400, blank=True)
   year_of_work = models.TextField(max_length=100, blank=True)
   date_created = models.DateTimeField(('date_created'), auto_now_add=True, blank=True)
   class Meta:
        abstract = True
        
class portfolios(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    # title = models.CharField( max_length=100,)
    description = models.TextField(max_length=600, blank=True)
    image = models.ImageField(upload_to='postimage/', null=True, blank=True)
    date_created = models.DateTimeField(('date_created'), auto_now_add=True, blank=True)

class artist_profile(pubemail, pubphone, profiletype, genders, portfolio):
 
 
#    dzongkha

   SELECT = 'select'
   BUMTHANG='Bumthang'
   CHUKHA='Chukha'
   DAGANA='Dagana'
   GASA='Gasa'
   HAA = 'Haa'
   LHUNTSE='Lhuntse'
   MONGAR='Mongar'
   PARO = 'Paro'
   PAMAGATSHEL='Pemagatshel'
   PUNAKHA='Punakha'
   SAMDRUP_JONGKHAR='Samdrup Jongkhar '
   SAMTSE='Samtse'
   SARPANG='Sarpang'
   THIMPHU = 'Thimphu'
   TRASHIGANG = 'Trashigang'
   TRASHIYANGTSE='Trashiyangtse'
   TRONGSA='Trongsa'
   TSIRANG='Tsirang'
   WANGDUE='Wangdue Phodrang'
   ZHEMGANG='Zhemgang'
   
   
   STATUS3 = [
       (SELECT, ('Select')),
       (BUMTHANG,('Bumthang')),
       (CHUKHA, ('Chukha')),
       (DAGANA, ('Dagana')),
       (GASA, ('Gasa')),
       (HAA , ('Haa')),
       (LHUNTSE, ('Lhuntse')),
       (MONGAR, ('Mongar')),
       (PARO , ('Paro')),
       (PAMAGATSHEL, ('Pemagatshel')),
       (PUNAKHA, ('Punakha')),
       (SAMDRUP_JONGKHAR, ('Samdrup Jongkhar ')),
       (SAMTSE, ('Samtse')),
       (SARPANG, ('Sarpang')),
       (THIMPHU, ('Thimphu')),
       (TRASHIGANG, ('Trashigang')),
       (TRASHIYANGTSE, ('Trashiyangtse')),
       (TRONGSA, ('Trongsa')),
       (TSIRANG, ('Tsirang')),
       (WANGDUE, ('Wangdue Phodrang')),
       (ZHEMGANG, ('Zhemgang')),
       
       
   ]

#  Employment  
   SELECT = 'select'
   EMPLOYED = 'Employed'
   UNEMPLOYED = 'Unemployed'
   STUDENT = 'Student'
   BUSINESS = 'Business'
   
   
   STATUS5 = [
       (SELECT, ('Select')),
       (EMPLOYED, ('Employed')),
       (UNEMPLOYED, ('Unemployed')),
       (STUDENT, ('Student')),
       (BUSINESS, ('Business')),
       
   ]



   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
#   portfo=portfolios.objects.filter(man=user).distinct()
#   portfolio= models.ForeignKey(portfolios, blank=True, on_delete=models.DO_NOTHING, default=1,  db_column="portfolio" )
   name = models.CharField(max_length=100, blank=False)
   pubprofile = models.ImageField(upload_to='avatars/', null=True, blank=True)
 
   pudDzongkhag = models.CharField( max_length=32, choices=STATUS3, default=SELECT,)
 
   pubemployment_status = models.CharField( max_length=32, choices=STATUS5, default=SELECT,)
  
   
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   is_bronze = models.BooleanField('Is bronze', default=False)
   is_silver = models.BooleanField('Is silver', default=False)
   is_gold = models.BooleanField('Is gold', default=False)
   ip_view = models.ManyToManyField(IpModel, related_name="post_view", blank=True)
   likes = models.ManyToManyField(IpModel, related_name="post_likes", blank=True)
# socail link
   facebook = models.CharField(max_length=300, blank=True)
   instagram = models.CharField(max_length=300, blank=True)
   youtube = models.CharField(max_length=300, blank=True)
#  Bio
   bio = models.TextField(max_length=200, blank=True)

   def total_views(self):
      return self.ip_view.count()

   def __str__(self):
       return self.name
   
#   @property
#   def description(self):
#       return self.portfolio.description
       
#   @property
#   def image(self):
#       return self.portfolio.image
      
   @property
   def ip(self):
       return self.ip_view.ip
   @property
   def is_approved(self):
       return self.user.is_approved

   @property
   def is_artscrafts(self):
       return self.user.is_artscrafts

   @property
   def is_fastival(self):
       return self.user.is_fastival
       
    
   @property
   def is_celebrations(self):
       return self.user.is_celebrations
       
       
   @property
   def is_historical(self):
       return self.user.is_historical
       
   @property
   def is_museums(self):
       return self.user.is_museums 
    
   @property
   def is_historical(self):
       return self.user.is_historical
    
   @property
   def is_libraries(self):
       return self.user.is_libraries

   @property
   def is_archives(self):
       return self.user.is_archives
   


    # Arts
   @property
   def is_painting(self):
       return self.user.is_painting
       
   @property
   def is_digital(self):
       return self.user.is_digital     
       
   @property
   def is_photography(self):
       return self.user.is_photography    
       
   @property
   def is_sculpture(self):
       return self.user.is_sculpture

   @property
   def is_pottery(self):
       return self.user.is_pottery

   @property
   def is_livemusic(self):
       return self.user.is_livemusic      
  
   @property
   def is_theater(self):
       return self.user.is_theater     
  
    
   @property
   def is_dance(self):
       return self.user.is_dance    
 
   @property
   def is_opera(self):
       return self.user.is_opera   
  
   @property
   def is_puppetry(self):
       return self.user.is_puppetry   
  

    # Media
   @property
   def is_book(self):
       return self.user.is_book   
  
   @property
   def is_magazines(self):
       return self.user.is_magazines  
  
   @property
   def is_comics(self):
       return self.user.is_comics 
            
   @property
   def is_film(self):
       return self.user.is_film 
            
        
   @property
   def is_television(self):
       return self.user.is_television
            
         
   @property
   def is_radio(self):
       return self.user.is_radio

   @property
   def is_musicvideo(self):
       return self.user.is_musicvideo           
        
   @property
   def is_digitalcontent(self):
       return self.user.is_digitalcontent           
        
      
   @property
   def is_digitalcontent(self):
       return self.user.is_digitalcontent           
        
         
   @property
   def is_software(self):
       return self.user.is_software         

   @property
   def is_videogames(self):
       return self.user.is_videogames         
        
   @property
   def is_animations(self):
       return self.user.is_animations        
        
    # function creation
   @property
   def is_fashion(self):
       return self.user.is_fashion        
        
   @property
   def is_jewellery(self):
       return self.user.is_jewellery       
                    
   @property
   def is_toys(self):
       return self.user.is_toys       
           
    
   @property
   def is_interiordesign(self):
       return self.user.is_interiordesign      
           
   @property
   def is_graphics(self):
       return self.user.is_graphics 
       
   @property
   def is_architecture(self):
       return self.user.is_architecture 
       
   @property
   def is_advertising(self):
       return self.user.is_advertising 
           
   
   @property
   def is_creativerd(self):
       return self.user.is_creativerd
           
   @property
   def is_creativeeventservices(self):
       return self.user.is_creativeeventservices
           
   @property
   def is_digitalservices(self):
       return self.user.is_digitalservices
              
         
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"
    