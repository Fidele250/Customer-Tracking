from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.forms import formset_factory
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from Accounts.models import *
from Accounts.forms import orderForm,customerForm,CreateUserForm,ProductForm,CreateMessage

from rest_framework.decorators import api_view
from rest_framework.response import Response
from Accounts.serializers import CustomerSerializer
from Accounts.filters import OrderFilter
from Accounts.decorators import allowed_user,admin_customer

# Create your views here.

@login_required(login_url='login')
@allowed_user(allowes_roles=['admin'])

def home(request):
    customers= Customer.objects.all().order_by('id')
    orders = Order.objects.all() 
    total_orders = orders.count()
    delivered = orders.filter(status ='Delivered').count()
    pending = orders.filter(status ='Pending').count()


    context = {'customers':customers,'orders':orders,'delivered':delivered,'pending': pending,'total_orders':total_orders}

    return render(request,'accounts/dashboard.html',context)

@login_required(login_url='login')
def product(request):
    product = Product.objects.all().order_by('id')
    return render(request,'accounts/products.html',{'product':product})

@login_required(login_url='login')
def customer(request,pk):
    customers= Customer.objects.get(id = pk)
    orderCount = customers.orders.count()
    orders= customers.orders.all()
    My_filter = OrderFilter(request.GET,queryset=orders)
    orders = My_filter.qs
    
    
    


    context = {"customers":customers,'orderCount':orderCount,'orders':orders,'my_filter':My_filter}
    
    return render(request,'accounts/customer.html',context)

@login_required(login_url='login')
def create_Order(request):
    form = orderForm()
    if request.method == 'POST':
        form =orderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
            
    context = {'form':form}
    return render(request,'accounts/order_template.html',context)
    
    
@login_required(login_url='login')
def update_Order(request,pk):
    form = orderForm()
    order = Order.objects.get(id = pk)
    if request.method == 'POST':
        form = orderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'accounts/order_template.html',context)


@login_required(login_url='login')
def delete_Order(request,pk):
    order = Order.objects.get(id = pk)
    if order:
        order.delete()
        return redirect('home')


@login_required(login_url ='login')
def customer_create(request):
    form = customerForm()
    context = {'form':form}
    if request.method == 'POST':
        form = customerForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request,'Customer created successful')
        return redirect('home')
    return render (request,'accounts/customer_template.html',context)

@login_required(login_url ='login')
def customer_update(request,pk):
    customers = Customer.get_object_or_404(Customer,id = pk)
    form = customerForm()
    if request.method == 'POST':
        form = customerForm(request.POST, instance= customers)
        if form.is_valid():
            form.save()
            return redirect('customer')
    else:
        form = customerForm() 
    
    context = {'form':form}
    return render(request,'accounts/customer_template.html',context) 


@login_required(login_url='login') 
@allowed_user(allowes_roles=['admin'])
def customer_delete(request,pk):
    customers = Customer.objects.get(id = pk)
    if customers:
         customers.delete()
         return redirect('home')
    else:
        messages.error(request,'Seems customer Does not exist')
    return render(request,'accounts/customer_template.html',{'custom':customers})
    
    
def login_view (request):
    if request.user.is_authenticated:# If user already loged in
         return redirect('/')
    else:
        if request.method == 'POST':
            username= request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username = username,password = password)

            if user is not None:
                login(request, user)
                if user.role =='Admin':
                    return redirect('landing')
                elif user.role =='Customer' :
                    return redirect('/')
            
        
            else:
                messages.info(request,'Either username or password is incorrect')
                return redirect('login')
        
    return render(request, 'accounts/login.html')

@login_required(login_url ='login')
def log_out(request):
    logout(request)
    return redirect('login')



def register (request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user =form.save()
            group = Group.objects.get(name = 'customer')
            user.groups.add(group)
            
            messages.success(request,  ' Created successfully' )
        return redirect('login')
    
    return render(request, 'accounts/registration.html', {'form':form})
    

### LANDING PAGE ###
def landing(request):
    return render(request, 'accounts/landing.html')

## PRODUCT VIEWS ##
@login_required(login_url='login')
@allowed_user(allowes_roles=['admin'])
def productCreate(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm()
    
    return render(request,'accounts/productCreate.html',{'form':form})


@login_required(login_url='login')
def send_message(request):
    if request.method == 'POST':
        form = CreateMessage(request.POST)
        if form.is_valid():
            message_obj = form.save(commit=False)
            message_obj.user = request.user
            message_obj.save()
            return redirect('pmessage')  
    else:
        form = CreateMessage(initial={'user': request.user})

            

    return render (request,'accounts/message.html',{
        'form': form,
        'user_email': request.user.email  
    })


@login_required(login_url='login')
def personal_message(request,pk):
    pmessage = Message.objects.get(id = pk)
    
    user = request.user
    context = {
        'pmessage':pmessage,
        'user':user
    }
    
    if pmessage.user != user and not user.is_staff:
       
        
        return HttpResponse('You have created no message')
    else:
        return render(request,'accounts/personal_message.html',context)
       
    
    



def userProfile(request):
    user = CustomUser.objects.all()
    

@api_view(['GET'])
def customerlist (request):
    customer = Customer.objects.all()
    for cust in customer:
        print(cust.name)

    serializer = CustomerSerializer(customer, many = True)
    return Response (serializer.data)




