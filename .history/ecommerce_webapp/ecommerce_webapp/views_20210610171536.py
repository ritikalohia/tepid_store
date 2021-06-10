from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# def tracker(request):
#     return render(request, 'shop/tracker.html')

def account(request):
    return render(request, "login_signin.html")

def productView(request):
    return render(request, "product_view.html")

def checkout(request):
    return render(request, 'shop/checkout.html')      