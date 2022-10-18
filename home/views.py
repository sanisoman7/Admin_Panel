from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import random
from . models import manager
# from . models import inspector_master
# from . models import manager
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password= request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('super_admin_panel')
        else :
            messages.info(request,'Invalid details')
            return redirect('/')
    else:
        return render (request,'login.html')
    # return render(request,'Login.html')
def super_admin_panel(request):
    
    return render(request,'super_admin.html')
    #-----------------------------------------------

def fn_manager(request):
    
    characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi@#$%^&*jklmnop0123456789qrstuvwxyz')        
    thepassword = ''
    for x in range(10):
        thepassword += random.choice(characters)
    return render(request,'manager.html',{"password":thepassword})

    # return render(request, 'manager.html')

def fn_coordinator(request):

    characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi@#$%^&*jklmnop0123456789qrstuvwxyz')        
    thepassword = ''
    for x in range(10):
        thepassword += random.choice(characters)
    return render(request,'coordinator.html',{"password":thepassword})


    # return render(request, 'coordinator.html')

def fn_inspectors(request):

    characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi@#$%^&*jklmnop0123456789qrstuvwxyz')        
    thepassword = ''
    for x in range(10):
        thepassword += random.choice(characters)
    return render(request,'inspectors.html',{"password":thepassword})


    # return render(request, 'inspectors.html')


def logout(request):
     auth.logout(request)
     return redirect('/')