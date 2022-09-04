from django.contrib import admin

from .models import *

class UserAdmin (admin.ModelAdmin):
    list_display = ["name", "role"]


    class Meta:
        model = User

admin.site.register(User, UserAdmin)
