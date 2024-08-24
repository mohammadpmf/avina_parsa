from django.contrib import admin

from .models import Customer, Product, Order, Comment

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ['first_name', 'last_name', 'birth_date', 'country', 'city', 'postal_code', 'number']
    list_display_links = ['first_name', 'last_name']
    list_editable = ['postal_code', 'number']
    ordering = ['country', 'city', 'last_name', 'first_name']
    list_filter = ['last_name', 'city']
    search_fields = ['last_name', 'city']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['customer', 'product', 'amount', 'datetime_created']
    ordering = ['-datetime_created']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment