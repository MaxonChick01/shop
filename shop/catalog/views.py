from django.shortcuts import render, redirect
from .models import *

def catalog(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'catalog.html', context=context)

def contacts(request):
    return render(request, 'contacts.html')

def conditions(request):
    return render(request, 'conditions.html')

def products(request, slug):
    category = Category.objects.get(slug=slug)
    objs = Item.objects.select_subclasses().filter(category=category)
    context = {'items': objs, 'category': category}
    return render(request, 'products.html', context=context)

def single_product(request, pk, slug):
    category = Category.objects.get(slug=slug)
    obj = Item.objects.select_subclasses().get(pk=pk)
    fields = {}
    for i in obj._meta.fields[6:]:
        fields[i.verbose_name] = getattr(obj, i.name)

    context = {'obj': obj, 'category': category, 'fields': fields}

    return render(request, 'single-product.html', context=context)
    
def usercart(request):
    return render(request, 'cart.html')

def order(request, pk):
    item = Item.objects.get(pk=pk)
    context = {'item': item}
    if request.method == 'POST':
        return render(redirect('catalog'))
    return render(request, 'order.html', context=context)