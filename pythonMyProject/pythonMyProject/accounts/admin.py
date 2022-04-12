from django.contrib import admin

from pythonMyProject.accounts.models import AppUser, Profile


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'date_joined', )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'user', )
