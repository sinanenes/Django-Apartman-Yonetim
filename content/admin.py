from django.contrib import admin

# Register your models here.
from content.models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


admin.site.register(Menu, MenuAdmin)
