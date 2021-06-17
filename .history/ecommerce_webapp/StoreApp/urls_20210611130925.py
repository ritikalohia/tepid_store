from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("account/", views.account, name="Account"),
    path("aboutus/", views.about, name="AboutUs"),
    path("contactus/", views.contact, name="Contact"),
    #path("tracker/", views.tracker, name="TrackingStatus"),
    path("producview/", views.productView, name="ProductView"),
    path("products/", views.products, name="Product"),
    path("checkout/", views.checkout, name="Checkout"),
    path("/", views.checkout, name="Checkout"),

]