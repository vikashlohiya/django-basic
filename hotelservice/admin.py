from django.contrib import admin
from hotelservice.models import Contactus  # Import your model
from django.contrib import admin

class ContactusAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')  # Specify fields to display in the list view



admin.site.register(Contactus,ContactusAdmin)


