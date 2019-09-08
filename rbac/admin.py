from django.contrib import admin
from .models import UserProfile, Organization, Role, Menu, Permission

admin.site.register(UserProfile)
admin.site.register(Organization)
admin.site.register(Role)
admin.site.register(Menu)
admin.site.register(Permission)

