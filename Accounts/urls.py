from django.http import HttpResponse
from django.urls import path
from Accounts import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('product/',views.product,name='product'),
    path('order/create/',views.create_Order,name="Create-order"),
    path('order/update/<str:pk>/',views.update_Order,name="Update-order"),
    path('order/delete/<str:pk>/',views.delete_Order,name="Delete-order"),
    path('customers/create/',views.customer_create,name="Create-customer"),

]