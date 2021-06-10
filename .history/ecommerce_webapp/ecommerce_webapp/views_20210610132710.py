from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return render(request, "")

def checkout(request):
    return render(request, 'shop/checkout.html')      