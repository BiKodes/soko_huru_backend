import datetime

from django.contrib import admin
from django.urls import reverse

from .models import Order, OrderItem

def order_name(obj):
    return '%s %s' % (obj.first_name, obj.last_name)
order_name.short_description = 'Name'

def admin_order_shipped(ModelAdmin, request, queryset):
    for order in queryset:
        order.shipped_date = datetime.datetime.now()
        order.status = Order.SHIPPED
        order.save()
    return
admin_order_shipped.short_description = 'Set shipped'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', order_name, 'status', 'created_at']
    list_filter = ['created_at', 'status']
    search_fields = ['first_name','mobile_number']
    inlines = [OrderItemInline]
    actions = [admin_order_shipped]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
