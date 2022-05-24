from django.contrib import admin

# Register your models here.
from payment.models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'year', 'month', 'payment', 'type', 'status', 'adminnote']
    list_filter = ['year', 'month', 'type', 'status']
    readonly_fields = ['user', 'payment', 'type']

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Payment, PaymentAdmin)
