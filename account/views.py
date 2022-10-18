from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout ,  update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# from requests import request

from account.forms import RegistrationForm, authForm


from django.http import HttpResponse
from django.shortcuts import  render



from django.contrib.sites.shortcuts import get_current_site
import random
# Create your views here.
from django.core.mail import EmailMessage
# send mail is not faster but EmailMessage is faster
from django.core.mail import send_mail
import threading
from account.models import User
# EmailThread is to speed up the send email
class EmailThread(threading.Thread):
     def __init__(self, email):
         self.email = email
         threading.Thread.__init__(self)
     def run(self):
         self.email.send(fail_silently=False)


def login_user(request):
    if request.method == "POST":
         email = request.POST['email']
         password = request.POST['password']
         user = authenticate(request, email=email, password=password)
         
         if user is not None and user.is_approved:
           login(request, user) 
           messages.success(request, ("you are  approved by admin"))
           if user is not None and user.is_heriages:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_arts:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_media:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_creation:
                login(request, user)
                return redirect('approved')
            

           elif user is not None and user.is_artscrafts:
                login(request, user)
                return redirect('approved')

           elif user is not None and user.is_fastival:
                login(request, user)
                return redirect('approved')
            
           elif user is not None and user.is_celebrations:
                login(request, user)
                return redirect('approved')

           elif user is not None and user.is_historical:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_museums:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_libraries:
                login(request, user)
                return redirect('approved')  
           elif user is not None and user.is_archives:
                login(request, user)
                return redirect('approved') 


           elif user is not None and user.is_painting:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_digital:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_photography:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_sculpture:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_pottery:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_livemusic:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_theater:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_dance:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_opera:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_puppetry:
                login(request, user)
                return redirect('approved')


           elif user is not None and user.is_book:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_magazines:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_comics:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_film:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_television:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_radio:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_musicvideo:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_digitalcontent:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_software:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_videogames:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_animations:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_fashion:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_jewellery:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_toys:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_interiordesign:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_graphics:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_architecture:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_advertising:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_creativerd:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_creativeeventservices:
                login(request, user)
                return redirect('approved')
           elif user is not None and user.is_digitalservices:
                login(request, user)
                return redirect('approved')
           else:
                msg= 'invalid credentials'
           return redirect('approved')
           
         elif user is not None and user.is_notapproved:
                login(request, user)
                # messages.success(request, ("you are not approved "))
                return redirect('notapproved')
         else:
            messages.success(request, ("There Was An Error In password/Email"))
            return redirect('login') 
    else:
       return render(request, 'auth/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You are logged out!"))
    return redirect('index')
        
      
def register_user(request):
     if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
                  form.save()
                  email = form.cleaned_data['email']
                  password = form.cleaned_data['password1']
                  password = form.cleaned_data['password2']
            
                  user = authenticate(email=email, password=password)
                  email_subject = 'Membership Status'
                  email_massage = f'Sign up successful. Please sign in and submit form.'
                  send_by = 'pemawangchuk177@gmail.com'
                  email = EmailMessage(
                    email_subject,
                    email_massage,
                    send_by,
                    [email]
                   )
                  EmailThread(email).start()
                  user.save()
                  return redirect('approved')
       
     else:
        #  return redirect('signup')
         form = RegistrationForm()
       

     return render(request, 'auth/sign_up.html', {
        'form':form,
    })
    


def verify(request):
    #  user = User.objects.get(user=request.user)
     user =User(email=email)
     if user.is_approved == True:
         user.save()
         email_subject = 'Subject here'
         email_massage = f'You are account has been approved, processed to create a profile.'
         send_by = 'pemawangchuk177@gmail.com'
         email = EmailMessage(
                    email_subject,
                    email_massage,
                    send_by,
                    [email]
                )
         user.save()
         EmailThread(email).start()
     else:
         email_subject = 'Subject here'
         email_massage = f'Registration failed. Please submit valid documents.'
         send_by = 'pemawangchuk177@gmail.com'
         email = EmailMessage(
                    email_subject,
                    email_massage,
                    send_by,
                    [email]
                )
         user.save()
         EmailThread(email).start()

         return HttpResponse('login.html' )
         
def save(self, *args,**kwargs):
       try:
          checking = User.objects.get(email = self.email)
          if checking.is_approved == False:
            print("mail send notapproved")
            checking.save(*args,**kwargs)
          else:
              print("hello")
              checking.save(*args,**kwargs) 
       except:
           print("okay")
def change_password(request):
    if request.method=="POST":
        form= PasswordChangeForm(data=request.POST, user=request.user)  
        if form.is_valid():
            update_session_auth_hash(request, form.user)  
            messages.success(request, " Password has successfully Changed")
            return redirect('home')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request, 'change_pass.html',{'form':form})
