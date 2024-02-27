from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse("This is my login")



def myaccount(request):
    return HttpResponse("Hi from account")    
