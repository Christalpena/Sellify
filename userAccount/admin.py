from django.contrib import admin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ('date_joined','last_login','followers')
admin.site.register(CustomUser,CustomUserAdmin)