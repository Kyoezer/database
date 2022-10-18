from django.contrib import admin

from app.models import   IpModel, artist_profile, authUser, portfolios, Subscriber


class AuthAdmin(admin.ModelAdmin):
     list_display = ('user',  'owner', 'cell_number','Dzongkhag', 'remarks', 'date_joined',  'is_staff', 'document', )
     search_fields = ( 'user', 'cell_number')
admin.site.register(authUser, AuthAdmin)

class profileadmin(admin.ModelAdmin):
     list_display = ('user', 'name','phone', 'pudDzongkhag', 'date_joined',   'pubprofile'  )
    #  search_fields = ('phone', 'name')
    
     # change_list_template = 'change_list_graph.html'
admin.site.register(artist_profile, profileadmin)

admin.site.register(IpModel)
admin.site.register(portfolios)
admin.site.register(Subscriber)

