from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    CAT=((1,'Mobile'),(2,'Colths'),(3,'Shoes'))
    name=models.CharField(max_length=50,verbose_name="Product Name")
    cat=models.IntegerField(verbose_name="Category",choices=CAT)
    price=models.FloatField(verbose_name="Product Price")
    status=models.BooleanField(default=True)
    pimage=models.ImageField(upload_to="image")
    
    # def __str__(self):

    #    return self.name
    
class Cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)

class Order(models.Model):
    order_id=models.IntegerField()
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField()

    def __str__(self):

        return self.order_id

class OrderHistory(models.Model):
    order_id=models.CharField(max_length=400)
    pay_id=models.CharField(max_length=400)
    sign=models.CharField(max_length=400)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
 
    def __str__(self):

        return self.order_id
