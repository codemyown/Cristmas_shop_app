from django.shortcuts import render
from django.http import HttpResponse
from .models.contact import Contact
from .models.product import Product
from .models.blog import Blog
from django.core.mail import send_mail

# Create your views here.

def index(request):
    
    
    send_mail(
        'testing mail',
        'welcome to us',
        'ajaypawar22112001@gmail.com',
        ['ajaypawar6225@gmail.com'],
        fail_silently=False
        )
    data = Product.get_all_products()
    mydata = Blog.get_all_Data()
    data  = {
        'data':data,
        'mydata':mydata
    }
    
    
    
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['phone']
        message = request.POST['message']
        my_contact = Contact(name = name,email = email,phone = number,
                            message = message)
        my_contact.save()
        
    return render(request,"index.html",data)