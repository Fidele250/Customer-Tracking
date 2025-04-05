from django.contrib import admin

# Register your models here.

from Accounts.models import Customer,Product,Order,Tag,CustomUser

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(CustomUser)


