from django.contrib import admin
from ecommapp.models import Product,OrderHistory,Order
# Register your models here.
#admin.site.register(Product)

class ProductAdminClass(admin.ModelAdmin):
    list_display=['name','cat','price','status']
    list_filter=['status','cat']

admin.site.register(Product,ProductAdminClass)
admin.site.register(OrderHistory)
admin.site.register(Order)
admin.site.site_header="Ekart Dashboard"