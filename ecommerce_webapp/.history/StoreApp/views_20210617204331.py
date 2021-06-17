from django.http import HttpResponse 
from django.shortcuts import render, redirect
from . models import Product, Account

#for cart
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

#for product page
from django.views.generic import ListView


def index(request):
    return render(request, 'index.html')

# def tracker(request):
#     return render(request, 'shop/tracker.html')

def account(request):
    if request.method=="POST":
        print(request)
        name = request.POST.get('name', ' ')
        email = request.POST.get('email', ' ')
        password = request.POST.get('password', ' ')
        account = Account(name=name, email=email, password=password)
        account.save()
    return render(request, "login_signin.html")


def productView(request):
    product = Product.objects.get(product_id = id){'product': product}
    return render(request, 'product_view.html')


def checkout(request):
    return render(request, 'checkout.html')    

def products(request):
    products = Product.objects.all()
    context={'prods': products}
    #print(products)
    return render(request, "products.html", context)

def about(request):
    return render(request, "aboutus.html")    


def contact(request):
    return render(request, "contact.html")       




#for cart
@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')