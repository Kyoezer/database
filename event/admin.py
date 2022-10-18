from django.contrib import admin

from event.models import addevent

# Register your models here.
# admin.site.register(addevent)

class eventadmin(admin.ModelAdmin):
     list_filter = ('owner',  'title', 'is_approved', 'create_date')
     list_display = ('owner',  'title', 'is_approved', )
     search_fields = ('owner',  'title', )
     ordering = ('title',)
admin.site.register(addevent, eventadmin)