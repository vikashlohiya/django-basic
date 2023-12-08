from django.shortcuts import render
from django.http import HttpResponse
from hotelservice.models import Contactus;
from django.conf import settings
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from .helper.utils import getMsg
from  base.model import printMsg
def home(request):
    # Render the template and return it as an HTML response
    print(settings.STATICFILES_DIRS)
   
    return render(request, 'home.html')


def aboutus(request):
    # Render the template and return it as an HTML response
    return render(request, 'aboutus.html')   

def contact(request):
    # Render the template and return it as an HTML response
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        message = request.POST.get('umessage')
        phone = request.POST.get('uphoneno')
        formdata={'name':name,'email':email,'message':message,'phone':phone}
        if not name or not email or not message or not phone:
            error_message = "All fields are required."
            return render(request, 'contactus.html', {'error_message': error_message,'formdata':formdata})
        elif len(phone)!=10:
            error_message = "Phone no should be 10 digits."
            return render(request, 'contactus.html', {'error_message': error_message,'formdata':formdata})
        else:
            contactdata=Contactus(name=name,email=email,message=message,phone=phone);  
            contactdata.save();  
            return render(request, 'contactus.html', {'success_message': 'Your request has been taken. We will call back you soon. Thankyou!'})

        
        
    return render(request, 'contactus.html') 


def loginpage(request):

    if request.method == 'POST':     
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        
        formdata={'uname':uname,'password':password}
        if not uname or not password:
            error_message = "All fields are required."
            messages.error(request, error_message)
            return render(request, 'login.html', {'error_message': error_message,'formdata':formdata})
        else:
             authenticated_user = authenticate( username=uname, password=password)
             print(authenticated_user)       
             if authenticated_user is None:
               messages.error(request, 'Invalid User')
               return render(request, 'login.html', {'formdata':formdata})   
             else:  
                 
               login(request,authenticated_user) 
               return redirect('home')  # Replace 'home' with the desired URL name or path

             
    
    return render(request,'login.html')

def signup(request):

    if request.method == 'POST':     
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        formdata={'uname':uname,'password':password,'fname':fname,'lname':lname,'email':email}
        if not uname or not password or not fname or not lname or not email:
          
            messages.error(request, 'All fields are required.')
            return render(request, 'signup.html', {'formdata':formdata})
        
        elif cpassword!=password:
            messages.error(request, 'Password does not match.')
            return render(request, 'signup.html', {'formdata':formdata})
        elif len(password)<6:
            messages.error(request, 'Password should be long at least 6 characters long.')
            return render(request, 'signup.html', {'formdata':formdata})
        elif User.objects.filter(username=uname).exists():
                messages.error(request, 'Username is taken')  
                return render(request, 'signup.html', {'formdata':formdata})
        elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is taken')  
                return render(request, 'signup.html', {'formdata':formdata})    
        else:
                # Create the user
                user = User.objects.create_user(username=uname, email=email, password=password,first_name=fname,last_name=lname)
               
                messages.success(request, 'Account created successfully')
                return render(request, 'signup.html')
    return render(request,'signup.html')

def logOutFun(request):
    logout(request)
    # Redirect to a specific URL after logout
    return redirect('home')  
    
