from django.contrib import admin
from .models import GFG


class GFGAdmin(admin.ModelAdmin):
    list_display = ['hotel_name' , 'hotel_price' , 'hotel_description'] # these are the fiedls that will the showen in the django.admin form

admin.site.register(GFG, GFGAdmin)




