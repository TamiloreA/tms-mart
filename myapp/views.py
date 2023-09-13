from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author
from django.db.models import Q
# Create your views here.
def index(request):
    # return HttpResponse('<h1>Welcome to our pyhton class</h1>')
    return render(request, 'hello.html')

def about(request):
    # return HttpResponse('<h1>This is our about us page</h1>')
    return render(request, 'destiny.html')

def contact(request):
    if request.method == "POST" : 
        print("form triggered")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        
        check_author = Author.objects.filter(Q(name__icontains=name) | Q(email__icontains=email)).exists()
        if check_author : 
            print("this user exists already")
            return render(request, 'hello.html')
        
        else :
            new_author = Author(name=name, email=email, phone=phone, password=password)
            new_author.save()
            
            print("New user added successfully")
            return render(request, 'hello.html')
    
            
    # return HttpResponse('<h1>This is our contact page</h1>')
    return render(request, 'signup.html')
 
def demo(request) : 
    pass 

def login(request):
    if request.method == "POST" : 
        print("form triggered")
        name = request.POST['name']
        password = request.POST['password']
        
        check_author = Author.objects.filter(Q(name__icontains=name) & Q(password__icontains=password)).exists()
        if check_author : 
            print("Successfully Login")
            return render(request, 'hello.html')
        else :
            print("Something went wrong...Don't have an account?")
            
            
    return render(request, 'registration.html')