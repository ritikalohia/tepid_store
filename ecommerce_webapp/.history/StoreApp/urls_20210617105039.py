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

     path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
]