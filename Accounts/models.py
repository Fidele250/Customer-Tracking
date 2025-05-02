from django.db import models
from django.contrib.auth.models import AbstractUser

from Customer import settings

# Create your models here.


class CustomUser(AbstractUser):
     role_choice = (
          ('Admin','Admin'),
          ('Customer','Customer'),
     )
     image = models.ImageField(error_messages='No Image',null=True)
     role =models.CharField(max_length=15,choices=role_choice,default='Customer')
     def __str__(self):
          return self.email
          

class Customer(models.Model):
    name = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    phone = models.CharField(max_length = 255,null=True)
    email = models.EmailField(null=True)
    date = models.DateField(auto_created=True,null=True,auto_now_add=True,editable=True)

    def __str__(self):
        return self.name.username
    
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
    customer =models.ForeignKey(Customer,null = True, on_delete = models.CASCADE,related_name='orders')
    product = models.ForeignKey(Product,null =True,on_delete=models.SET_NULL,related_name='products')
    date = models.DateField(auto_created=True)
    status = models.CharField(max_length=255,choices =STATUS)
    def __str__(self):
            return f'{self.product.name} ordered by {self.customer.name}'
    

class Message (models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE,default=False,null=False)
     message = models.TextField()
     class Meta:
          def __str__(self):
               return f'message from {self.user}'



