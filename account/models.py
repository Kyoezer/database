
from datetime import timezone
from django.core.mail import EmailMessage
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from django.contrib.auth.base_user import BaseUserManager

from django.db.models.signals import ( post_save, pre_save)
from django.dispatch import receiver

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
       
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, **extra_fields)
import threading

# EmailThread is to speed up the send email
class EmailThread(threading.Thread):
     def __init__(self, email):
         self.email = email
         threading.Thread.__init__(self)
     def run(self):
         self.email.send(fail_silently=False)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True,)
    is_active = models.BooleanField(('active'), default=True)
    is_staff = models.BooleanField(('staff'), default=False)
    is_approved= models.BooleanField('Is approved', default=True)
    is_deny = models.BooleanField('Is deny', default=False)
    is_notapproved = models.BooleanField('Is notapproved', default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_heriages= models.BooleanField('Is heriages', default=False)
    is_arts = models.BooleanField('Is arts', default=False)
    is_media = models.BooleanField('Is media', default=False)
    is_creation = models.BooleanField('Is creation', default=False)

    # heritages
    is_artscrafts = models.BooleanField('Is Arts crafts', default=False)
    is_fastival = models.BooleanField('Is fastival', default=False)
    is_celebrations = models.BooleanField('Is celebrations', default=False)
    is_historical = models.BooleanField('Is historical', default=False)
    is_museums = models.BooleanField('Is museums', default=False)
    is_libraries = models.BooleanField('Is libraries', default=False)
    is_archives = models.BooleanField('Is archives', default=False)

    # Arts
    is_painting = models.BooleanField('Is painting', default=False)
    is_digital = models.BooleanField('Is digital', default=False)
    is_photography = models.BooleanField('Is photography', default=False)
    is_sculpture = models.BooleanField('Is sculpture', default=False)
    is_pottery = models.BooleanField('Is pottery', default=False)
    is_livemusic = models.BooleanField('Is live music', default=False)
    is_theater = models.BooleanField('Is theater', default=False)
    is_dance = models.BooleanField('Is dance', default=False)
    is_opera = models.BooleanField('Is opera', default=False)
    is_puppetry = models.BooleanField('Is puppetry', default=False)

    # Media
    is_book = models.BooleanField('Is book', default=False)
    is_magazines = models.BooleanField('Is magazines', default=False)
    is_comics = models.BooleanField('Is comics', default=False)
    is_film = models.BooleanField('Is film', default=False)
    is_television = models.BooleanField('Is television', default=False)
    is_radio = models.BooleanField('Is radio', default=False)
    is_musicvideo = models.BooleanField('Is music video ', default=False)
    is_digitalcontent = models.BooleanField('Is digital content', default=False)
    is_software = models.BooleanField('Is software', default=False)
    is_videogames = models.BooleanField('Is video games', default=False)
    is_animations = models.BooleanField('Is animations', default=False)

    # function creation
    is_fashion = models.BooleanField('Is fashion', default=False)
    is_jewellery = models.BooleanField('Is jewellery', default=False)
    is_toys = models.BooleanField('Is toys', default=False)
    is_interiordesign = models.BooleanField('Is interior design', default=False)
    is_graphics = models.BooleanField('Is graphics', default=False)
    is_architecture = models.BooleanField('Is architecture', default=False)
    is_advertising = models.BooleanField('Is advertising', default=False)
    is_creativerd = models.BooleanField('Is creative R&D', default=False)
    is_creativeeventservices = models.BooleanField('Is creative event services', default=False)
    is_digitalservices = models.BooleanField('Is creative digital services', default=False)
    
    
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta: 
        verbose_name = ('user')
        verbose_name_plural = ('users')
    #signal used for is_active=False to is_active=True
@receiver(pre_save, sender=User)
def active(sender, instance, **kwargs):
    if instance.is_approved and User.objects.filter(pk=instance.pk, is_approved=True).exists():
        print('send emil')
        subject = 'Active account'
        message = '%s your account is now active' %(instance.email)
        from_email = 'creativebhutan@gov.bt'
        mail=EmailMessage(
                    subject, 
                    message, 
                    from_email, 
                    [instance.email],
                    # fail_silently=False
                )
        EmailThread(mail).start()
    else:
        pass
        # subject = 'Account Status'
        # message = '%s Registration failed. Please submit valid documents.' %(instance.email)
        # from_email = 'pemawangchuk177@gmail.com'
        # mail=EmailMessage(
        #             subject, 
        #             message, 
        #             from_email, 
        #             [instance.email],
        #             # fail_silently=False 
        #         )
        # EmailThread(mail).start()

@receiver(pre_save, sender=User)
def active(sender, instance, **kwargs):
    if instance.is_deny and User.objects.filter(pk=instance.pk, is_deny=True).exists():
        print(' emil')
        subject = 'account deny '
        message = '%s Registration failed. Please submit valid documents.'  %(instance.email)
        from_email = 'creativebhutan@gov.bt '
        mail=EmailMessage(
                    subject, 
                    message, 
                    from_email, 
                    [instance.email],
                    # fail_silently=False
                )
        EmailThread(mail).start()   

# signal to send an email to the admin when a user creates a new account
@receiver(post_save, sender=User, dispatch_uid='register')
def register(sender, instance, **kwargs):
    if kwargs.get('created', False):
        subject = 'Verification of the %s account' %(instance.email)
        message = 'New User'
        from_email = 'creativebhutan@gov.bt'
        mail=EmailMessage(subject, message, from_email, [from_email],)
        EmailThread(mail).start()
        

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)



