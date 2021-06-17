from email.policy import default
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_priority = models.IntegerField(default="4")
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default="0")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to = "images", default="")

    def __str__(self):
        return self.product_name


class Account(models.Model):
    user_id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70, default="")
    password = models.CharField(max_length=70, default="")
  
    def __str__(self):
        return self.name        