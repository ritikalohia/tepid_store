from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("account/", views.account, name="Account"),
    #path("contact/", views.contact, name="Contact"),
    #path("tracker/", views.tracker, name="TrackingStatus"),
    path("producview/", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
]