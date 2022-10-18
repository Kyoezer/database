from django.contrib import admin

from heriage.models import arch_post, arts_craft_post, authHeritage, autharch, autharts, authceles, authfestival, authhistorical, authlabrary, authmuseum, cele_post, festival_post, heriage_post, historical_post, labrary_post, museum_post

# # Register your models here.
admin.site.register(heriage_post)

class AuthAdmin(admin.ModelAdmin):
     list_display = ('user',  'owner', 'phone_no', 'remarks', 'date_joined',  'is_staff', 'skills',  'document', )
     search_fields = ( 'user', 'phone_no',)
admin.site.register(authHeritage, AuthAdmin)

admin.site.register(arts_craft_post)
admin.site.register(autharts)

admin.site.register(festival_post)
admin.site.register(authfestival)

admin.site.register(cele_post)
admin.site.register(authceles)

admin.site.register(historical_post)
admin.site.register(authhistorical)

admin.site.register(museum_post)
admin.site.register(authmuseum)

admin.site.register(labrary_post)
admin.site.register(authlabrary)

admin.site.register(arch_post)
admin.site.register(autharch)
