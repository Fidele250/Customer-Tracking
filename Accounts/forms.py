from django.forms import ModelForm
from Accounts.models import Order,Customer

class orderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer','product','status','date']


class customerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name','phone','email','date']

    