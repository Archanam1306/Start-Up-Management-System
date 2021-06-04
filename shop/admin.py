from django.contrib import admin
from .models import Shop, Product, Advertisement
from image_cropping import ImageCroppingMixin

class ShopAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'owner_name', 'shop_type', 'is_published', 'list_date')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    search_fields = ('name', 'owner_name', 'shop_type', 'tag')
    list_per_page = 20

class ProductAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'shop', 'product_type', 'is_published', 'is_mvp', 'list_date')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_published','is_mvp',)
    list_editable = ('is_published','is_mvp',)
    search_fields = ('name', 'shop', 'product_type', 'tag', 'category')
    list_per_page = 20

class AdvertisementAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('id', 'ad_name', 'shop', 'approved_by', 'is_published','list_date')
    list_display_links = ('id', 'ad_name')
    prepopulated_fields = {'slug': ('ad_name',)}
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    search_fields = ('ad_name', 'shop', 'approved_by')
    list_per_page = 20


admin.site.register(Shop,ShopAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Advertisement,AdvertisementAdmin)