from django.contrib import admin

# Register your models here.
from content.models import Menu, Content, Imagen


class ContentImagenInline(admin.TabularInline):
    model = Imagen
    extra = 5


class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'menu', 'type', 'image_tag', 'status']
    list_filter = ['status', 'menu']
    inlines = [ContentImagenInline]
    readonly_fields = ('image_tag',)


class ImagenAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'image_tag']
    list_filter = ['content']
    readonly_fields = ('image_tag',)


admin.site.register(Menu, MenuAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Imagen, ImagenAdmin)
