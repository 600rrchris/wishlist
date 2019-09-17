from django.shortcuts import render
from .models import Item
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse


# Create your views here.
def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'

class ItemDelete(DeleteView):
    model = Item
    fields = '__all__'
    success_url = '/'

