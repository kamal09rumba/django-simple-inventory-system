from django.contrib import admin

# import item models
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount'] #without list_display it uses name of the model in our case Item object

admin.site.register(Item,ItemAdmin)