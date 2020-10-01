from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})



def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request,'product_details.html', {'product':product})

def product_upload(request):
    form = ProductForm()
    if request.method == "POST":
         form = ProductForm(request.POST,request.FILES)
         if form.is_valid():
            form.save()
         return redirect('products-list')
         
    else:
       form = ProductForm()
       return render(request, 'upload_product.html', {'form': form})
  



   