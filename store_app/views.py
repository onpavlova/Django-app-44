from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, Category
from .forms import ProductForm, ProductModelForm, ProductDeleteForm

def index(request):
    """Главная страница."""
    return render(request, 'store_app/index.html')

def about(request):
    """Страница о нас."""
    return HttpResponse('<h1>About us!</h1>')

def product_list(request):
    """Список товаров"""
    products = Product.objects.all()
    context = {
        'title': 'Список товаров',
        'products': products,
    }
    return render(request, 'store_app/product_list.html', context=context)

def product_detail(request, product_id):
    """Cтраница для одного товара."""
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'store_app/product_detail.html', context=context)

def product_add(request):
    """Представление для добавления нового товара"""
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form =  ProductModelForm()

    context = {
        'form': form,
        'title': 'Добавить товар'
    }
    return render(request, 'store_app/product_add.html', context=context)

def product_edit(request, product_id):
    """Представление для редактирования товара."""

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductModelForm(instance=product)

    context = {
        'form': form,
        'title': 'Изменить товар'
    }
    return render(request, 'store_app/product_edit.html', context=context)
