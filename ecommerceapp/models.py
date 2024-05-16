from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=255,null=True)
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    product_name=models.CharField(max_length=255,null=True)
    product_description=models.CharField(max_length=255,null=True)
    product_price=models.IntegerField(null=True)
    product_image=models.ImageField(upload_to="image/", null=True)

class Userdetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    user_address=models.CharField(max_length=255,null=True)
    user_number=models.CharField(max_length=255,null=True)
    user_image=models.ImageField(upload_to="image/" ,null=True)


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(default=1,null=True)
    def total_price(self):
        return self.quantity*self.product.product_price

