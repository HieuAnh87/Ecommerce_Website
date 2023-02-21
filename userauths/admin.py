from django.contrib import admin
from userauths.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'bio', 'is_staff', 'is_active')
    list_display_links = ('username', 'email')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    list_per_page = 25


admin.site.register(User, UserAdmin)  # register the custom user model
