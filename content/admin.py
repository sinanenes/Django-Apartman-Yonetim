from django.contrib import admin

# Register your models here.
from content.models import Menu, Content


class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'menu', 'type', 'status']
    list_filter = ['status', 'menu']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Content, ContentAdmin)
