from django.contrib import admin
from .models import LoginData

# Customize the admin interface for the LoginData model
class LoginDataAdmin(admin.ModelAdmin):
    list_display = ('username', 'mobile_number',  'email')  
    search_fields = ('username', 'mobile_number','email')  

# Register the model and the customized admin interface
admin.site.register(LoginData, LoginDataAdmin)
