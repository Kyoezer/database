from django.contrib import admin

from landingpage.models import copy_right, landind_page, logo, operate, quote

# Register your models here.
admin.site.register(landind_page)
admin.site.register(logo)
admin.site.register(operate)
admin.site.register(copy_right)
admin.site.register(quote)
