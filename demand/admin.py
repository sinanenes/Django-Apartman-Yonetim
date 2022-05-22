from django.contrib import admin

# Register your models here.
from demand.models import Demand


class DemandAdmin(admin.ModelAdmin):
    list_display = ['user', 'type', 'subject', 'detail', 'adminnote', 'status']
    list_filter = ['type', 'status']
    readonly_fields = ['user', 'subject', 'detail']

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Demand, DemandAdmin)
