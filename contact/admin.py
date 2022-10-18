from django.contrib import admin

from contact.models import  admincontact, publiccontact

# Register your models here.
# admin.site.register(publiccontact)
class pubadmin(admin.ModelAdmin):
    #  list_filter = ('submit_date',)
     list_display = ('first_name', 'email', 'phone', 'title', 'user',)
     search_fields = ('email', 'phone',)
    #  ordering = ('title',)
admin.site.register(publiccontact, pubadmin)

class eventadmin(admin.ModelAdmin):
    #  list_filter = ('submit_date',)
     list_display = ('name', 'phone',)
     search_fields = ('name', 'phone',)
    #  ordering = ('title',)
admin.site.register(admincontact, eventadmin)

