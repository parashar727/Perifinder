from django.contrib import admin

# Register your models here.
from .models import Item, Keyboard, Listing, Vendor

admin.site.register(Item)
admin.site.register(Keyboard)
admin.site.register(Listing)
admin.site.register(Vendor)