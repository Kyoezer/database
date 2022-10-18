from django.contrib import admin

from functional_creation.models import advertising_post, architecture_post, auth_advertising, auth_architecture, auth_creation, auth_creative_event_service, auth_creative_research_and_development, auth_digital_creative, auth_graphic, authfe,  authjew, authset_design, authtoy, creation_post, creative_event_service_post, creative_research_and_development_post, digital_service_post, fepost, graphic_post, jewpost, set_designpost, toypost

# Register your models here.
admin.site.register(creation_post)

class AuthAdmin(admin.ModelAdmin):
     list_display = ('user',  'owner', 'phone_no', 'remarks', 'date_joined',  'is_staff', 'skills',  'document', )
     search_fields = ( 'user', 'phone_no',)
admin.site.register(auth_creation, AuthAdmin)

admin.site.register(fepost)
admin.site.register(authfe)

admin.site.register(jewpost)
admin.site.register(authjew)

admin.site.register(toypost)
admin.site.register(authtoy)

admin.site.register(set_designpost)
admin.site.register(authset_design)

admin.site.register(graphic_post)
admin.site.register(auth_graphic)

admin.site.register(architecture_post)
admin.site.register(auth_architecture)

admin.site.register(advertising_post)
admin.site.register(auth_advertising)

admin.site.register(creative_research_and_development_post)
admin.site.register(auth_creative_research_and_development)

admin.site.register(creative_event_service_post)
admin.site.register(auth_creative_event_service)

admin.site.register(digital_service_post)
admin.site.register(auth_digital_creative)