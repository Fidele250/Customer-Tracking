from django.db import models
from django.contrib.auth.models import AbstractUser

from Customer import settings

# Create your models here.


class CustomUser(AbstractUser):
     role_choice = (
          ('Admin','Admin'),
          ('Customer','Customer'),
     )
     role =models.CharField(max_length=15,choices=role_choice,default='Customer')
     def __str__(self):
          return self.first_name
          

class Customer(models.Model):
    name = models.ForeignKey(CustomUser,max_length = 255,null=False,on_delete=models.CASCADE)
    phone = models.CharField(max_length = 255,null=True)
    email = models.EmailField(null=True)
    date = models.DateField(auto_created=True,null=True)

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
    



# class UserManager(BaseUserManager):
#      def createUser(self,username,email,password=None,**extra_fields):
#           if not email:
#                raise ValueError('Email shoul be provided')
#           email = self.normalize_email(email)
#           user = self.model(username=username,email = email,**extra_fields) 
#           user.set_password(password)
#           user.save(using =self.db)
#           return user
#      def CreateSuperUser(self,username,email,password = None,**extra_field):
#           extra_field.setdefault('is_staff',True)
#           extra_field.setdefault('is_superuser',True)
#           return createUser(self,username,email,password,**extra_fields)
     

# class CustomUser(AbstractUser):
 
#      email = models.EmailField(unique=True)
#      phone = models.CharField(max_length=15,unique=True)

#      objects = UserManager()

#      class Meta:
#           verbose_name_plural = 'Users'
#           verbose_name = 'User'
#      def __str__(self):
#           return self.username



