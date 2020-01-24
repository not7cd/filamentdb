from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from filaments.models import Material, Spool, Variant, OwnerProfile

# Register your models here.
admin.site.register(Material)
admin.site.register(Spool)
admin.site.register(Variant)


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class OwnerProfileInline(admin.StackedInline):
    model = OwnerProfile
    can_delete = False
    verbose_name_plural = 'owner'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (OwnerProfileInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
