from rest_framework import serializers
from Accounts.models import Customer

class CustomerSerializer(serializers.Serializer):
    class Meta:
        model = Customer
        fields = ['name','phone','email','date']