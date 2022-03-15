from django.contrib import admin
from .models import *
# Register your models here.

class UserManager(admin.ModelAdmin):
    list_display = ['id','username','nickname']
    list_display_links = ['username']
    
    
admin.site.register(User,UserManager)