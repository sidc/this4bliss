from django.contrib import admin
from django.forms import ModelForm, TextInput
from django.contrib.admin import ModelAdmin
from .models import Item, Tag
import autocomplete_light

# Register your models here.


class ItemAdmin(ModelAdmin):
    ## raw ids for search widget on foreign key relationships 
    ## https://docs.djangoproject.com/en/dev/ref/contrib/admin/
    raw_id_fields = ("related_item","publisher",) 
    ## On the change list page, this option allows tabular display. 
    list_display = ("title","publish_date","category_type","item_type","publisher","approval")
    ## On the right side of change list, this allows filtering the list
    list_filter = ("category_type","item_type")
    ## Search through these fields
    search_fields = ("title","publisher__name")


admin.site.register(Item, ItemAdmin)
admin.site.register(Tag)