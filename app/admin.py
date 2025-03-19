from django.contrib import admin
from app.models import Customers, Partner, Application, Product, ProductImage, ProductCharacteristic, Category


# Register your models here.
@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position', 'deascription')
    list_display_links = ('id', 'full_name', 'position', 'deascription')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'url', 'order')
    list_display_links = ('id', 'image', 'url', 'order')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'status')
    list_display_links = ('id', 'full_name', 'phone', 'status')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id',)



@admin.register(ProductCharacteristic)
class ProductCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Category)
class CatageryAdmin(admin.ModelAdmin):
    list_display = ('id',)

