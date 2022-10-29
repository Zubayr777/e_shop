from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=35)
    add_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=110)
    product_price = models.FloatField()
    product_des = models.TextField()
    product_count = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField(upload_to='media', null=True, blank=True)
    def __str__(self):
        return self.product_name

class UserCart(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_product_quantity = models.IntegerField()
    cart_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_id

