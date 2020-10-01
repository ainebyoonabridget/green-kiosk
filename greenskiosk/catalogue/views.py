from django.shortcuts import render
from .models import Product
from django.http import request
# from .models import Product
from .forms import ProductForm


# Create your views here.

def products_list(request):
    products = Product.objects.all()
    return render(request,'products_list.html',{'products':products})


def product_description(request,product_id):
    product = Product.objects.get(id=product_id)
    return render(request,'product_description.html',{'product':product})

def upload_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
    
        if form.is_valid():
            form.save()
        else:
            form = ProductForm
   
    return render(request, 'upload_product.html', {'form': form})
    