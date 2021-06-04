from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import WishList
from shop.models import Advertisement, Shop, Product
import json
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@csrf_protect
def login(request):
    if  request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

@csrf_protect
def register(request):
    if  request.method=='POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username already exist!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That E-mail is being used!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                    first_name=first_name, last_name=last_name)
                    auth.login(request, user)
                    messages.success(request, 'You are now registered and logged in!')
                    return redirect('index')
                    # user.save()
                    # messages.success(request, 'You are now registered and can log in!')
                    # return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if  request.method=='POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def wishlist(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        shop = request.POST['shop']
        product = request.POST['product']
        add = request.POST['add']
        if request.user.is_authenticated:
            user_id = request.user.id
            try:
                is_available = WishList.objects.get(user_id_id=user_id)
            except WishList.DoesNotExist:
                is_available = None
            if is_available:
                jsonDec = json.decoder.JSONDecoder()
                Wlist = jsonDec.decode(is_available.wish_list)
                if add == "1":
                    Wlist.append(product_id)
                if add == "0":
                    Wlist.remove(product_id)
                is_available.wish_list = json.dumps(Wlist)
                is_available.save()
            else:
                Wlist=[]
                if add == "1":
                    Wlist.append(product_id)
                Wlist_2 = json.dumps(Wlist)
                newuser = WishList(user_id=request.user, wish_list=Wlist_2)
                newuser.save()
    return redirect('/shop/'+shop+'/'+product)

def dashboard(request):
    productList = Product.objects.all().order_by('-list_date').filter(is_published=True)
    tour_data=[]
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
                tour_data=[]
            else:
                for i in Wlist:
                    data = productList.filter(id=int(i))
                    if data:
                        tour_data.append(data)
    paginator = Paginator(tour_data, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    print(tour_data)
    context={'productList':paged_listings, 'title': "Your WishList"}
    return render(request, 'accounts/dashboard.html', context)