from django.shortcuts import render, redirect
from homepage.models import Item
from django.views.generic import ListView, DetailView

# Create your views here.

def index(request):
    items = Item()
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})
"""
def show(request):
    items = Item()
    items = Item.objects.all()
    return render(request, 'index.html', {'items':items})
"""
def Aboutus(request):
    return render(request, 'aboutus.html')

def News(request):
    return render(request, 'news.html')

def Offers(request):
    return render(request, 'offers.html')
"""
def buynow(request):
    text = "Payment gateway will be added soon"
    return render(request, 'buynow.html', {'text' : text})
"""
def searchbar(request):
    return render(request, 'dropdown.html')

def itemdetails(request, itemid):
    item = Item.objects.get(pk= itemid)

    return render(request, "itemdetails.html", {'item': item})
    