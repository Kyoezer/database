
from django.db import models
from account.models import User
# from django.utils.timezone import now
# from multiselectfield import MultiSelectField

from app.models import artist_profile, pubemail, pubphone

# from app.models import pubemail, pubphone

class addevent(pubphone, pubemail):
   
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   title= models.CharField(max_length=100, blank=False)
   image_event = models.ImageField(upload_to='event/')
   dis= models.TextField(max_length=300, blank=True)
   create_date = models.DateTimeField( auto_now_add=True, blank=True)
   start_date = models.DateField(auto_now_add=False, blank=False)
   end_date = models.DateField(auto_now_add=False, blank=False)
   is_approved = models.BooleanField(('show'), default=False)
   
  
   

   