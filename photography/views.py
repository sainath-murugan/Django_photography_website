from django.shortcuts import render, redirect
from .forms import CustomerOrderForm
from django.contrib import messages
from .models import *

# Create your views here.
#sundar
#sundar-12345 in sqlite3
#sundar12345 in rds

def home(request):
    gallery = TotalImages.objects.all() #multiple data can be fetched, but only 18 photos will we display circulating all data from database
    title = IndexTitle.objects.first()
    service = IndexServices.objects.first()
    service_type = IndexServiceType.objects.first()
    title_and_number = IndexNumber.objects.all()
    return render(request, "index.html", {"gallery":gallery, "title":title, "service": service,"service_type": service_type, "title_and_number": title_and_number})

def services(request):
    service = IndexServices.objects.first()
    service_type = IndexServiceType.objects.first()
    return render(request, "services.html", {"service_type":service_type, "service":service})

def about(request):
    member = AboutUs.objects.all()
    return render(request, "about.html", {"details": member})

def gallery(request):
    wedding = TotalImages.objects.filter(image_category="wedding").first()
    wildlife = TotalImages.objects.filter(image_category="wildlife").first()
    modelling = TotalImages.objects.filter(image_category="modelling").first()
    product = TotalImages.objects.filter(image_category="products").first()
    event = TotalImages.objects.filter(image_category="events").first()    
    image = [wedding,wildlife,modelling,product,event]
    return render(request, "gallery.html",{"images":image})

def wildlife(request):
    image = TotalImages.objects.filter(image_category="wildlife").all()
    return render(request, "wildlife.html",{"images":image})
def modelling(request):
    image = TotalImages.objects.filter(image_category="modelling").all()
    return render(request, "modelling.html",{"images":image})
def events(request):
    image =TotalImages.objects.filter(image_category="events").all()    
    return render(request, "events.html",{"images":image})
def wedding(request):
    image = TotalImages.objects.filter(image_category="wedding").all()
    return render(request, "wedding.html",{"images":image})
def products(request):
    image = TotalImages.objects.filter(image_category="products").all()
    return render(request, "products.html",{"images":image})


def contact(request):
    form = CustomerOrderForm()
    address = Address.objects.first()
    if request.method == "POST":
        form = CustomerOrderForm(request.POST)
        if form.is_valid():
            detail = form.save()
            name = form.cleaned_data.get("name")
            messages.success(request, f"thank you for messaging us {name}, our team member will contact you soon")
            return redirect("home")
    return render(request, "contact.html", {"address": address, "form":form})

def videos(request):
    video = Videos.objects.all()
    return render(request, "video.html", {"videos":video})
