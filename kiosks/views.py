from django.shortcuts import render, redirect
from .models import Kiosk
from .forms import KioskForm,KioskOwnerForm


def kiosk_upload(request):
    form = KioskForm()
    if request.method == "POST":
         form = KioskForm(request.POST,request.FILES)
         if form.is_valid():
            form.save()
         return redirect('products-list')
         
    else:
       form = KioskForm()
       return render(request, 'upload_kiosk.html', {'form': form})
  
def kioskOwner_upload(request):
    form = KioskOwnerForm()
    if request.method == "POST":
         form = KioskOwnerForm(request.POST,request.FILES)
         if form.is_valid():
            form.save()
         return redirect('products-list')
         
    else:
       form = KioskForm()
       return render(request, 'upload_kiosk_owner.html', {'form': form})
  
