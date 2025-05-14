from django.contrib import admin
from .models import Product, Category, cart, Total_Cart, Contact, Billing_Address
# Register your models here.


class product(admin.ModelAdmin):
    list_display = ('sno', 'Active', 'Product_Name', 'Total_Stock', 'Availability', 'Discount_Price',  'Category', 'date')


class Cart(admin.ModelAdmin):
    list_display = ('sno', 'Merchant_Email', 'Product_Sno', 'Product_Name', 'Price', 'Qty', 'date')


class total_cart(admin.ModelAdmin):
    list_display = ('sno', 'Merchant_Email', 'Total_Item', 'Total_Price', 'date')


class contact(admin.ModelAdmin):
    list_display = ('sno', 'First_name', 'Last_name', 'Phone', 'Email', 'date')


class Billing_address(admin.ModelAdmin):
    list_display = ('sno', 'Status', 'Merchant_mail', 'Prices', 'City', 'Phone', 'date')


admin.site.register(Product,  product)
admin.site.register(Category)
admin.site.register(cart, Cart)
admin.site.register(Total_Cart, total_cart)
admin.site.register(Contact, contact)
admin.site.register(Billing_Address, Billing_address)
