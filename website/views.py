
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
# Create your views here.
def home(request):

    #check i floggin in
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        #authentiacte
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"you have been logged in")
            return redirect('home')
        else:
            messages.error(request,"there was an error while logging in")
            return redirect('home')
    else:
        return render(request,'home.html',{})
    
        

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been Logged Out succesfully')
    return redirect('home')

def register_user(request):
    return render(request,'register.html',{} )


    
