from django.http import HttpResponse 
from django.shortcuts import render
from . models import Product


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
        contact = account(name=name, email=email, password=password)
        contact.save()
    return render(request, "login_signin.html")

def productView(request):
    return render(request, "product_view.html")

def checkout(request):
    return render(request, 'shop/checkout.html')    

def products(request):
    products = Product.objects.all()
    context={'products': products}
    #print(products)
    return render(request, "products.html", context)