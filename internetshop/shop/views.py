

from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    print(request.GET)
    search = request.GET.get('search')

    products = Product.objects.all()
    if search:
        products = Product.objects.filter(name__contains=search).all()
    else:
        products = Product.objects.all()

    return render(request, "index.html", {

        'products': products,
        'search': search,
    })

def view_product(request, id):
    return render(request, 'products.html')