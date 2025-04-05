from django.http import HttpResponse
from django.urls import path
from Accounts import views

urlpatterns = [
    path('home/',views.home, name = 'home'),
    path('',views.landing,name ='landing'),
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('product/',views.product,name='product'),
    path('product/create/',views.productCreate,name = 'create_product'),
    path('order/create/',views.create_Order,name="Create-order"),
    path('order/update/<str:pk>/',views.update_Order,name="Update-order"),
    path('order/delete/<str:pk>/',views.delete_Order,name="Delete-order"),
    path('customers/create/',views.customer_create,name="Create-customer"),
    path('customers/delete/<str:pk>/',views.customer_delete,name = "Delete-customer"),
    path('customers/serializer/list/',views.customerlist),
    path ('login/',views.login_view,name = 'login'),
    path ('logout/',views.log_out,name = 'logout'),
    path('register/',views.register,name = 'register'),

]