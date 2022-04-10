from django.contrib import admin

# Register your models here.
from content.models import Menu, Content, Imagen


class ContentImagenInline(admin.TabularInline):
    model = Imagen
    extra = 5


class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'menu', 'type', 'status']
    list_filter = ['status', 'menu']
    inlines = [ContentImagenInline]


class ImagenAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'image']
    list_filter = ['content']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Imagen, ImagenAdmin)
