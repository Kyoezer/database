

# from typing_extensions import Self
from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import User
from app.models import artist_profile, authUser, portfolios
from arts.models import art_post, authart, authdance, authdigital, authlive, authopera, authpaint, authphoto, authpot, authpup, authsulp, auththe, dance_post, digital_post, live_post, opera_post, paint_post, photo_post, pot_post, pup_post, sulp_post, the_post
from contact.models import admincontact,publiccontact
from event.models import addevent
from functional_creation.models import advertising_post, architecture_post, auth_advertising, auth_architecture, auth_creation, auth_creative_event_service, auth_creative_research_and_development, auth_digital_creative, auth_graphic, authfe,  authjew, authset_design, authtoy, creation_post, creative_event_service_post, creative_research_and_development_post, digital_service_post, fepost, graphic_post,  jewpost, set_designpost, toypost
from heriage.models import arch_post, arts_craft_post, authHeritage, autharch, autharts, authceles, authfestival, authhistorical, authlabrary, authmuseum, cele_post, festival_post, heriage_post, historical_post, labrary_post, museum_post
from mediaapp.models import animation_post, auth_animation, auth_book, auth_digital_content, auth_media, auth_music_video, auth_software, auth_video_game, book_post, digital_content_post, media_post, music_video_post, software_post, video_game_post


class RegistrationForm(UserCreationForm):
	"""docstring for RegistrationForm"""
	email = forms.EmailField(required=True)
	# first_name = forms.CharField(max_length=30, required=True)
	# last_name = forms.CharField(max_length=100, required=True)


	class Meta: # define a metadata related to this class
		model = User
		fields = ( 
			'email',
			'first_name',
			'last_name',
			'password1',
			'password2',
			'is_heriages',
			'is_arts', 
			'is_media',
			'is_creation',
            'is_artscrafts',
            'is_fastival', 
            'is_celebrations',
            'is_historical', 
            'is_museums', 
            'is_libraries', 
            'is_archives',
            'is_painting', 
            'is_digital', 
            'is_photography', 
            'is_sculpture', 
            'is_pottery', 
            'is_livemusic', 
            'is_theater',
            'is_dance', 
            'is_opera', 
            'is_puppetry', 
            'is_book', 
            'is_magazines', 
            'is_comics', 
            'is_film', 
            'is_television',
            'is_radio', 
            'is_musicvideo', 
            'is_digitalcontent', 
            'is_software', 
            'is_videogames', 
            'is_animations',
            'is_fashion', 
            'is_jewellery', 
            'is_toys', 
            'is_interiordesign', 
            'is_graphics', 
            'is_architecture', 
            'is_advertising',
            'is_creativerd', 
            'is_creativeeventservices', 
            'is_digitalservices'

		)

	def save(self, commit=True,  *arg, ** awrgs,):
		user = super(RegistrationForm, self).save(commit=True)
		if commit:
			user.save( *arg, ** awrgs)
		return user
    

class auth_Formuser(forms.ModelForm):

    class Meta:
        model = authUser
        fields = ('cell_number','Dzongkhag','employment_status', 'document',) 
        
class portfolio_post(forms.ModelForm):
    class Meta:
        model = portfolios
        fields = ('description','image') 

class artist_Form(forms.ModelForm):

    class Meta:
        model = artist_profile
        fields = ( 'name', 'pubprofile', 'mail', 'is_show_mail',  'phone','is_show', 'gender', 'pudDzongkhag','pubemployment_status', 'profile_type', 'bio', 'facebook', 'instagram', 'youtube')

 
class heriageForm(forms.ModelForm):

    class Meta:
        model = heriage_post
        fields = ('title', 'type', 'image', 'discription')

class authHertiageFrom(forms.ModelForm):

    class Meta:
        model = authHeritage
        fields = ('phone_no', 'skills',  'document',) 

# arts crafts
class artsForm(forms.ModelForm):

    class Meta:
        model = arts_craft_post
        fields = ('title', 'image', 'discription')

class authartscrafts(forms.ModelForm):

    class Meta:
        model = autharts
        fields = ('phone_no', 'document',) 
# festival

class festivalForm(forms.ModelForm):

    class Meta:
        model = festival_post
        fields = ('title', 'image', 'discription')

class authfestivals(forms.ModelForm):

    class Meta:
        model = authfestival
        fields = ('phone_no', 'document',) 

# celebration
class dashForm(forms.ModelForm):

    class Meta:
        model = cele_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = authceles
        fields = ('phone_no', 'document',) 

# historical
class dashForm(forms.ModelForm):

    class Meta:
        model = historical_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = authhistorical
        fields = ('phone_no', 'document',)
# museum
class dashForm(forms.ModelForm):

    class Meta:
        model = museum_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = authmuseum
        fields = ('phone_no', 'document',)
# labraries
class dashForm(forms.ModelForm):

    class Meta:
        model = labrary_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = authlabrary
        fields = ('phone_no', 'document',)
# archives
class dashForm(forms.ModelForm):

    class Meta:
        model = arch_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = autharch
        fields = ('phone_no', 'document',)

# 

class artpost(forms.ModelForm):

    class Meta:
        model = art_post
        fields = ('title', 'type', 'image', 'discription')


class authartFrom(forms.ModelForm):

    class Meta:
        model = authart
        fields = ('phone_no', 'skills',  'document',) 

# painting
class dashForm(forms.ModelForm):

    class Meta:
        model = paint_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = authpaint
        fields = ('phone_no', 'document',)
#  digital arts

class dashForm(forms.ModelForm):

    class Meta:
        model = digital_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = authdigital
        fields = ('phone_no', 'document',)

# photography

class dashForm(forms.ModelForm):

    class Meta:
        model = photo_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = authphoto
        fields = ('phone_no', 'document',)

# scul

class dashForm(forms.ModelForm):

    class Meta:
        model = sulp_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = authsulp
        fields = ('phone_no', 'document',)

# pottery

class dashForm(forms.ModelForm):

    class Meta:
        model = pot_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = authpot
        fields = ('phone_no', 'document',)

# live video
class dashForm(forms.ModelForm):

    class Meta:
        model = live_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = authlive
        fields = ('phone_no', 'document',)

# theater
class dashForm(forms.ModelForm):

    class Meta:
        model = the_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = auththe
        fields = ('phone_no', 'document',)

# dance
class dashForm(forms.ModelForm):

    class Meta:
        model = dance_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = authdance
        fields = ('phone_no', 'document',)

# opera
class dashForm(forms.ModelForm):

    class Meta:
        model = opera_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = authopera
        fields = ('phone_no', 'document',)

# pup
class dashForm(forms.ModelForm):

    class Meta:
        model = pup_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = authpup
        fields = ('phone_no', 'document',)
# 


class mediapost(forms.ModelForm):

    class Meta:
        model = media_post
        fields = ('title', 'type', 'image', 'discription')


class authmediaFrom(forms.ModelForm):

    class Meta:
        model = auth_media
        fields = ('phone_no', 'skills',  'document',) 

# book
class dashForm(forms.ModelForm):

    class Meta:
        model = book_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = auth_book
        fields = ('phone_no', 'document',)

# music video
class dashForm(forms.ModelForm):

    class Meta:
        model = music_video_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = auth_music_video
        fields = ('phone_no', 'document',)

# digital content
class dashForm(forms.ModelForm):

    class Meta:
        model = digital_content_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = auth_digital_content
        fields = ('phone_no', 'document',)




# software
class dashForm(forms.ModelForm):

    class Meta:
        model = software_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = auth_software
        fields = ('phone_no', 'document',)

# video game
class dashForm(forms.ModelForm):

    class Meta:
        model = video_game_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = auth_video_game
        fields = ('phone_no', 'document',)

# video game
class dashForm(forms.ModelForm):

    class Meta:
        model = animation_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = auth_animation
        fields = ('phone_no', 'document',)
# 


class creationpost(forms.ModelForm):

    class Meta:
        model = creation_post
        fields = ('title', 'type', 'image', 'discription')


class authcreationFrom(forms.ModelForm):

    class Meta:
        model = auth_creation
        fields = ('phone_no', 'skills',  'document',) 

# fesion
class dashForm(forms.ModelForm):

    class Meta:
        model = fepost
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = authfe
        fields = ('phone_no', 'document',)

# gew
class dashForm(forms.ModelForm):

    class Meta:
        model = jewpost
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):

    class Meta:
        model = authjew
        fields = ('phone_no', 'document',)

# toy
class dashForm(forms.ModelForm):

    class Meta:
        model = toypost
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):
 
    class Meta:
        model = authtoy
        fields = ('phone_no', 'document',)

# set design

class dashForm(forms.ModelForm):

    class Meta:
        model = set_designpost
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):
 
    class Meta:
        model = authset_design
        fields = ('phone_no', 'document',)

# graphic
class dashForm(forms.ModelForm):

    class Meta:
        model = graphic_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):
 
    class Meta:
        model = auth_graphic
        fields = ('phone_no', 'document',)


# architure
class dashForm(forms.ModelForm):

    class Meta:
        model = architecture_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):
 
    class Meta:
        model = auth_architecture
        fields = ('phone_no', 'document',)
         
# advertising
class dashForm(forms.ModelForm):

    class Meta:
        model = advertising_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):
 
    class Meta:
        model = auth_advertising
        fields = ('phone_no', 'document',)
    
# create RD
class dashForm(forms.ModelForm):

    class Meta:
        model = creative_research_and_development_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):
 
    class Meta:
        model = auth_creative_research_and_development
        fields = ('phone_no', 'document',)



# creative event and  service
class dashForm(forms.ModelForm):

    class Meta:
        model = creative_event_service_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):
 
    class Meta:
        model = auth_creative_event_service
        fields = ('phone_no', 'document',)


# digital service
class dashForm(forms.ModelForm):

    class Meta:
        model = digital_service_post
        fields = ('title', 'image', 'discription')

class authForm(forms.ModelForm):
 
    class Meta:
        model = auth_digital_creative
        fields = ('phone_no', 'document',)
# 

class event_form(forms.ModelForm):
   
    class Meta:
        model = addevent
        fields = ('title', 'phone', 'is_show', 'mail', 'is_show_mail',  'image_event','dis', 'start_date','end_date') 


class contactform(forms.ModelForm):
  
    class Meta:
        model = publiccontact
        fields = ('email','first_name', 'last_name', 'phone', 'discription') 


class adminform(forms.ModelForm):
  
    class Meta:
        model = admincontact
        fields = ( 'name', 'email','phone', 'discription') 

