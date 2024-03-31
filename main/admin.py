from main.models import Users, Banners, Favourite, Favouriteitem, Products, Shop, ShopItem, UserPhone, Blogs, Categories, Salesproduct
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'birthday', 'phone', 'address', 'photo')}),
        (_('Permissions'), {
            'fields': (
            'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_client'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = (
        'id', 'username', 'first_name', 'last_name', 'phone', 'birthday', 'is_superuser',
        'is_client')
    list_display_links = ('id', 'username')

admin.site.register(Users, UserAdmin)
admin.site.register(Products)
admin.site.register(Banners)
admin.site.register(Shop)
admin.site.register(ShopItem)
admin.site.register(Favourite)
admin.site.register(Favouriteitem)
admin.site.register(UserPhone)
admin.site.register(Blogs)
admin.site.register(Categories)
admin.site.register(Salesproduct)

