from django.contrib import admin
from users.models import User
from django.contrib.admin import ModelAdmin

# Register your models here.

class UserAdmin(ModelAdmin):
	## On the change list page, this option allows tabular display. 
    list_display = ("name","email","location","mentor_user")
    ## On the right side of change list, this allows filtering the list
    list_filter = ("location","mentor_user")
    ## Search through these fields
    search_fields = ("name","mentor_user__name")

admin.site.register(User, UserAdmin)