from django.db import models
from datetime import datetime
from image_cropping import ImageRatioField
from PIL import Image
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True, max_length=200)
    shop_type = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    profile_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    profile_photo_crop = ImageRatioField('profile_photo', '270x303')
    feature_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    feature_photo_crop = ImageRatioField('feature_photo', '470x620')
    slider_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    slider_photo_crop = ImageRatioField('slider_photo', '1030x550')
    description_1 = RichTextField()
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    photo_1_crop = ImageRatioField('photo_1', '330x250')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    photo_2_crop = ImageRatioField('photo_2', '330x250')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    photo_3_crop = ImageRatioField('photo_3', '330x250')
    description_2 = RichTextField(blank=True, null=True)
    tag = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200, blank=True)
    twitter = models.CharField(max_length=200, blank=True)
    instagram = models.CharField(max_length=200, blank=True)
    youtube = models.CharField(max_length=200, blank=True)
    owner_name = models.CharField(max_length=200)
    owner_view = RichTextField(blank=True, null=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop', args=[self.slug])


class Product(models.Model):
    shop = models.ForeignKey(Shop, default = 1, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True, max_length=200)
    product_type = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    is_mvp = models.BooleanField(default=True)
    profile_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    profile_photo_crop = ImageRatioField('profile_photo', '270x303')
    original_rate = models.IntegerField(blank=0)
    discounted_rate = models.IntegerField(blank=True, null=True)
    description_1 = RichTextField()
    is_size = models.BooleanField(default=True)
    category= models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1_crop = ImageRatioField('photo_1', '440x520')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_2_crop = ImageRatioField('photo_2', '440x520')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_3_crop = ImageRatioField('photo_3', '440x520')
    description_main = RichTextField()
    description_image = models.ImageField(upload_to='photos/%Y/%m/%d')
    description_image_crop = ImageRatioField('description_image', '369x460')
    stock_available = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    size = models.CharField(max_length=200, blank=True)
    color = models.CharField(max_length=200, blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', args=[self.shop.slug,self.slug])

class Advertisement(models.Model):
    shop = models.ForeignKey(Shop, default = 1, on_delete=models.CASCADE)
    ad_name = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True, max_length=200)
    is_published = models.BooleanField(default=True)
    approved_by = models.CharField(max_length=200)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.ad_name