from django.contrib import admin

from pythonMyProject.bikes.models import Bike, SellBike, Order, OrderItem, ShippingAddress


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_created', 'user', )


@admin.register(SellBike)
class SellBikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'frame', 'fork', 'rear_shock', 'brakes', 'drivetrain', 'price', 'date_created',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'complete', 'transaction_id', 'date_ordered')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order_id', 'quantity', 'date_added', )


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    # list_display = ('customer', 'order', 'address', 'city', 'country', 'zipcode', 'date_added', )
    pass
