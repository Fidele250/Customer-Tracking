from django import forms
from django.forms import ModelForm
from Accounts.models import Order,Customer,CustomUser,Product,Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import Textarea, TextInput ,EmailInput


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

class CreateMessage(ModelForm):
    class Meta:
        model = Message
        fields = [ 'message']
        widgets = {
            'message': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type a message here ...',
                'rows': 8,
                'style': 'resize: none;',  # Disable resizing
                'name':'email',
                'label: ':'Message',
            }),

        }