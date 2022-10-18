from django.contrib import admin

from arts.models import art_post, authart, authdance, authdigital, authlive, authopera, authpaint, authphoto, authpot, authpup, authsulp, auththe, dance_post, digital_post, live_post, opera_post, paint_post, photo_post, pot_post, pup_post, sulp_post, the_post

# Register your models here.
admin.site.register(art_post)

class AuthAdmin(admin.ModelAdmin):
     list_display = ('user',  'owner', 'phone_no', 'remarks', 'date_joined',  'is_staff', 'skills',  'document', )
     search_fields = ( 'user', 'phone_no',)
admin.site.register(authart, AuthAdmin)

admin.site.register(paint_post)
admin.site.register(authpaint) 

admin.site.register(digital_post)
admin.site.register(authdigital)

admin.site.register(photo_post)
admin.site.register(authphoto)

admin.site.register(sulp_post)
admin.site.register(authsulp)

admin.site.register(pot_post)
admin.site.register(authpot)

admin.site.register(live_post)
admin.site.register(authlive)

admin.site.register(the_post)
admin.site.register(auththe)

admin.site.register(dance_post)
admin.site.register(authdance)

admin.site.register(opera_post)
admin.site.register(authopera)

admin.site.register(pup_post)
admin.site.register(authpup)