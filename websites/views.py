#website views.py
from django.shortcuts import render
from shop.models import Advertisement, Shop, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    ads = Advertisement.objects.filter(is_published=True).order_by('-list_date')[:2]
    if len(ads)==2:
        ad_shop_1 = Shop.objects.get(id=ads[0].shop.id)
        ad_products_1 = Product.objects.filter(shop=ads[0].shop.id).filter(is_published=True).order_by('-list_date')
        ad_shop_2 = Shop.objects.get(id=ads[1].shop.id)
        ad_products_2 = Product.objects.filter(shop=ads[1].shop.id).filter(is_published=True).order_by('-list_date')
        context ={ 'ad_shop_1':ad_shop_1, 'ad_products_1':ad_products_1, 'ad_shop_2':ad_shop_2, 'ad_products_2':ad_products_2}
        return render(request,"pages/index.html", context)
    else:
        return render(request,"pages/index.html")

def cart(request):
    return render(request,"pages/shopping-cart.html")

def faq(request):
    return render(request,"pages/faq.html")

def contact(request):
    return render(request,"pages/contact.html")

def checkout(request):
    return render(request,"pages/check-out.html")

def blog(request):
    return render(request,"pages/blog.html")

def post(request):
    return render(request,"pages/blog-details.html")

def search(request):
    productList = Product.objects.all().order_by('-list_date').filter(is_published=True)
    final_search_list =[]
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        temp=[]
        ref_list=[]
        if keyword:
            ref = Shop.objects.all().filter(name__icontains=keyword)
            if ref:
                for t in ref:
                    ref_list.append(t.id)
                for i in ref_list:
                    temp.append(productList.filter(shop=i))
            temp.append(productList.filter(name__icontains=keyword))
            temp.append(productList.filter(description_1__icontains=keyword))
            temp.append(productList.filter(description_main__icontains=keyword))
            temp.append(productList.filter(tag__icontains=keyword))
            temp.append(productList.filter(category__icontains=keyword))
            temp.append(productList.filter(product_type__icontains=keyword))
            if temp:
                for s in temp:
                    if s:
                        for k in s:
                            final_search_list.append(k)
    final_search_list = set(final_search_list)
    paginator = Paginator(list(final_search_list), 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context={'productList':paged_listings, 'title': "Search results for \""+request.GET['keyword']+"\""}
    return render(request,"pages/shopProducts.html", context)