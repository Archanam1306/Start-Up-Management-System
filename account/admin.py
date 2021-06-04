from django.contrib import admin
from .models import WishList
from image_cropping import ImageCroppingMixin
# Register your models here.

class WishListAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(WishList,WishListAdmin)