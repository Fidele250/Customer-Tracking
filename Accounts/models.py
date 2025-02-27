from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length = 255,null=True)
    phone = models.CharField(max_length = 255,null=True)
    email = models.EmailField(null=True)
    date = models.DateField(auto_created=True,null=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    TAG =(('Sport','Sport'),
          ('Kitchen','Kitchen'),
          ('Beauty','Beauty')
          )
    name = models.CharField(max_length = 255,null=True,choices=TAG)
    

    def __str__(self):
        return self.name
    

class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor'),
    )
    
    name = models.CharField(max_length =255)
    price = models.IntegerField(null=True)
    category = models.CharField(max_length =255, choices= CATEGORY)
    description = models.CharField(max_length =255, null = True)
    date = models.DateField(auto_created=True)
    tag = models.ManyToManyField(Tag,related_name='tag')
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered')
    )
    customer =models.ForeignKey(Customer,null = True, on_delete = models.SET_NULL,related_name='orders')
    product = models.ForeignKey(Product,null =True,on_delete=models.SET_NULL)
    date = models.DateField(auto_created=True)
    status = models.CharField(max_length=255,choices =STATUS)
    def __str__(self):
            return f'{self.product.name} ordered by {self.customer.name}'