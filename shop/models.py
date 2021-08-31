from django.db import models
from django.db.models.base import Model

# Create your models here.
class Product(models.Model):
    product_Id = models.AutoField
    prodcut_name = models.CharField(max_length=20)
    category = models.CharField(max_length=30, default='')
    sub_category = models.CharField(max_length=30, default='')
    price = models.IntegerField(default=0)
    prodcut_description = models.CharField(max_length=50)
    publish_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default='')
    
    def __str__(self):
        return self.prodcut_name
    
class contact(models.Model):
    msg_Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=11,default='')
    query_txt = models.CharField(max_length=50, default='')
    
    def __str__(self):
        return self.name
    
class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items = models.CharField(max_length=100, default='')
    total_price = models.CharField(max_length=100, default='')
    
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=50,default='')
    city = models.CharField(max_length=15, default='')
    state = models.CharField(max_length=15, default='')
    zip = models.CharField(max_length=6,default='')

    def __str__(self):
        return 'order' + '(' + str(self.order_id)  + ')'
    
class update_order(models.Model):
    update_order_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(max_length=10)
    update_desc = models.CharField(max_length=100)
    timestamps = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc + '(' + str(self.order_id) + ')'
    