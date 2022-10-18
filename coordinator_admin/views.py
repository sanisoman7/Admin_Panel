from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import random

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

def fun_coordinator(request):

    characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi@#$%^&*jklmnop0123456789qrstuvwxyz')        
    thepassword = ''
    for x in range(10):
        thepassword += random.choice(characters)
    return render(request,'coordinator.html',{"password":thepassword})
def logout(request):
     auth.logout(request)
     return redirect('/')