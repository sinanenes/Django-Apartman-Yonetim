from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from demand.models import Demand


class DemandAdmin(admin.ModelAdmin):
    list_display = ['user', 'type', 'subject', 'adminnote', 'status']
    list_filter = ['type', 'status']
    readonly_fields = ['user', 'subject']

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Demand, DemandAdmin)
