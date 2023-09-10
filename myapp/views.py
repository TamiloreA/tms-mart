from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('<h1>Welcome to our pyhton class</h1>')
    return render(request, 'hello.html')

def about(request):
    # return HttpResponse('<h1>This is our about us page</h1>')
    return render(request, 'destiny.html')
def contact(request):
    # return HttpResponse('<h1>This is our contact page</h1>')
     return render(request, 'registration.html')
 
def demo(request) : 
    pass 