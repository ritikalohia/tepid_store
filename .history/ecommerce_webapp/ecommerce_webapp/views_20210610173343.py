from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# def tracker(request):
#     return render(request, 'shop/tracker.html')

def account(request):
    if request.method=="POST":
        print(request)
        name = request.POST.get('name', ' ')
        email = request.POST.get('email', ' ')
        subject = request.POST.get('subject', ' ')
        message = request.POST.get('message', ' ')
        contact = Account(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, "login_signin.html")

def productView(request):
    return render(request, "product_view.html")

def checkout(request):
    return render(request, 'shop/checkout.html')      