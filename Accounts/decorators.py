from django.shortcuts import redirect
from django.http import HttpResponse

def oneTwo(view_func):
    def oneThree(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request,*args,**kwargs)
    return oneThree()

# Decorators to let user login based on a role

# For admin only
def allowed_user(allowes_roles =[]):
    def decorator(view_function):
        def wrapper_function(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowes_roles:
                return view_function(request,*args,**kwargs)
            else:
                return HttpResponse('Need admin Permission 😊')
        return wrapper_function 
    return decorator

#Decorator for customer and admin

def admin_customer(allowes_roles =[]):
    def decorator(view_function):
        def wrapper_function(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group =='customer':
                return redirect('home')
                
            if group =='admin':
                return view_function(request,*args,**kwargs)
        return wrapper_function 
    return decorator
        
