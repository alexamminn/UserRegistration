from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(models_user_registration)
class admin_user_registration(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'last_login')
    search_fields = ('username', 'email')
    readonly_fields = ('last_login', 'join_date')
    fieldsets = ()
    list_filter = ()
    