from django.forms import ModelForm
from Accounts.models import Order,Customer,CustomUser,Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class orderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer','product','status','date']


class customerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name','phone','email','date']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','category','description','date','tag']

    
class CreateUserForm(UserCreationForm):
    class Meta:
         model =  CustomUser
         fields = ['username','email','role','password1','password2',]