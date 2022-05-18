from django.contrib import admin

# Register your models here.
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from content.models import Menu, Content, Imagen, Comment


class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)


class ContentImagenInline(admin.TabularInline):
    model = Imagen
    extra = 5


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'menu', 'type', 'image_tag', 'status', 'create_at']
    list_filter = ['status', 'menu', 'type']
    inlines = [ContentImagenInline]
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}


class ImagenAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'image_tag']
    list_filter = ['content']
    readonly_fields = ('image_tag',)


class MenuAdminTree(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_contents_count', 'related_contents_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Menu.objects.add_related_count(
            qs,
            Content,
            'menu',
            'contents_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Menu.objects.add_related_count(qs,
                                            Content,
                                            'menu',
                                            'contents_count',
                                            cumulative=False)
        return qs

    def related_contents_count(self, instance):
        return instance.contents_count

    related_contents_count.short_description = 'Related contents (for this specific category)'

    def related_contents_cumulative_count(self, instance):
        return instance.contents_cumulative_count

    related_contents_cumulative_count.short_description = 'Related contents (in tree)'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'content', 'user', 'status']
    list_filter = ['status']


# admin.site.register(Menu, MenuAdmin)
# admin.site.register(Menu, MPTTModelAdmin)
admin.site.register(Menu, MenuAdminTree)
admin.site.register(Content, ContentAdmin)
admin.site.register(Imagen, ImagenAdmin)
admin.site.register(Comment, CommentAdmin)
