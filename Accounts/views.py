from django.shortcuts import render,redirect
from django.http import HttpResponse
from Accounts.models import *
from Accounts.forms import orderForm,customerForm
# Create your views here.


def home(request):
    customers= Customer.objects.all().order_by('id')
    orders = Order.objects.all() 
    total_orders = orders.count()
    delivered = orders.filter(status ='Delivered').count()
    pending = orders.filter(status ='Pending').count()


    context = {'customers':customers,'orders':orders,'delivered':delivered,'pending': pending,'total_orders':total_orders}

    return render(request,'accounts/dashboard.html',context)

def product(request):
    product = Product.objects.all().order_by('id')
    return render(request,'accounts/products.html',{'product':product})

def customer(request,pk):
    customers= Customer.objects.get(id = pk)


    context = {"customers":customers}
    
    return render(request,'accounts/customer.html',context)


def create_Order(request):
    form = orderForm()
    if request.method == 'POST':
        form =orderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/')
            
    context = {'form':form}
    return render(request,'accounts/order_template.html',context)
    
    
def update_Order(request,pk):
    form = orderForm()
    order = Order.objects.get(id = pk)
    if request.method == 'POST':
        form = orderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'accounts/order_template.html',context)


def delete_Order(request,pk):
    order = Order.objects.get(id = pk)
    if order:
        order.delete()
        return redirect('/')


def customer_create(request):
    form = customerForm()
    context = {'form':form}
    if request.method == 'POST':
        form = customerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render (request,'accounts/customer_template.html',context)

