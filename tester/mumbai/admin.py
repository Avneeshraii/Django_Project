from django.contrib import admin
from mumbai.models import AddClient


# class Addclient(admin.ModelAdmin):
#     list_display=('name','email','phone','address')


admin.site.register(AddClient)