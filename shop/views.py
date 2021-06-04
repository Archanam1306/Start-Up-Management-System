from django.shortcuts import render
from .models import Shop, Product
from account.models import WishList
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

def shop(request, shop):
    shop_detail = Shop.objects.get(slug=shop)
    product_details = Product.objects.filter(shop=shop_detail.id).filter(is_mvp=True).order_by('-list_date')[:4]
    context = {'shop':shop_detail, 'productDetails':product_details}
    return render(request,"pages/shopDetail.html", context)

def shoplist(request):
    shopList = Shop.objects.filter(is_published=True).order_by('-list_date')
    paginator = Paginator(shopList, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context={'shopList':paged_listings}
    return render(request,"pages/shopList.html", context)


def shopProducts(request):
    productList = Product.objects.filter(is_published=True).order_by('-list_date')
    paginator = Paginator(productList, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context={'productList':paged_listings, 'title': "All Products"}
    return render(request,"pages/shopProducts.html", context)

def product(request, product, shop):
    product_detail = Product.objects.get(slug=product)
    add=False
    if request.user.is_authenticated:
        user_id = request.user.id
        try:
            is_available = WishList.objects.get(user_id_id=user_id)
        except WishList.DoesNotExist:
            is_available = None
        if is_available:
            jsonDec = json.decoder.JSONDecoder()
            Wlist = jsonDec.decode(is_available.wish_list)
            if not Wlist:
                add=False
            if str(product_detail.id) in Wlist:
                add=True
            else:
                add=False
    context = {'product': product_detail, 'add':add}
    return render(request,"pages/productDetail.html", context)

def shopProductsList(request, shop):
    shop_detail = Shop.objects.get(slug=shop)
    productList = Product.objects.filter(shop=shop_detail.id).filter(is_published=True).order_by('-list_date')
    paginator = Paginator(productList, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context={'productList':paged_listings, 'title': shop_detail.name + " Products"}
    return render(request,"pages/shopProducts.html", context)