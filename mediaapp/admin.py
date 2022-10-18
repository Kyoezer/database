from django.contrib import admin

from mediaapp.models import animation_post, auth_animation, auth_book, auth_com, auth_digital_content, auth_fil, auth_media, auth_music_video, auth_rad, auth_software, auth_tele, auth_video_game, book_post, com_post, digital_content_post, fil_post, maga_book, maga_post, media_post, music_video_post, rad_post, software_post, tele_post, video_game_post

# Register your models here.
admin.site.register(media_post)

class AuthAdmin(admin.ModelAdmin):
     list_display = ('user',  'owner', 'phone_no', 'remarks', 'date_joined',  'is_staff', 'skills',  'document', )
     search_fields = ( 'user', 'phone_no',)
admin.site.register(auth_media, AuthAdmin)

admin.site.register(book_post)
admin.site.register(auth_book)

admin.site.register(maga_post)
admin.site.register(maga_book)

admin.site.register(com_post)
admin.site.register(auth_com)

admin.site.register(fil_post)
admin.site.register(auth_fil)

admin.site.register(tele_post)
admin.site.register(auth_tele)

admin.site.register(rad_post)
admin.site.register(auth_rad)

admin.site.register(music_video_post)
admin.site.register(auth_music_video)

admin.site.register(digital_content_post)
admin.site.register(auth_digital_content)

admin.site.register(software_post)
admin.site.register(auth_software)

admin.site.register(video_game_post)
admin.site.register(auth_video_game)

admin.site.register(animation_post)
admin.site.register(auth_animation)
