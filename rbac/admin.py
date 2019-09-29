from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserInfo, Role, Menu, Permission

class UserAdmin(UserAdmin):
    #重写fieldsets在admin后台加入自己新增的字段
    fieldsets = (
        (None, {'fields': ('username','real_name','image', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Roles'), {'fields': ('roles',)}),
    )

admin.site.register(UserInfo, UserAdmin)
admin.site.register(Role)
admin.site.register(Menu)
admin.site.register(Permission)

