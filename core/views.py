from django.db.models import Count
from django.shortcuts import render
from core.models import Product, Category, CartOrder, CartOrderItems, ProductReviews, Wishlist, Address, ProductImages, \
    Vendor


def index(request):
    # products = Product.objects.all().order_by('-id')

    products = Product.objects.filter(featured=True, product_status='published').order_by('-id')
    context = {
        'products': products
    }
    return render(request, "core/index.html", context)


def product_list_view(request):
    products = Product.objects.filter(product_status='published').order_by('-id')
    context = {
        'products': products
    }
    return render(request, "core/product_list.html", context)


def category_list_view(request):
    categories = Category.objects.all().annotate(total_products=Count('product'))
    context = {
        'categories': categories
    }
    return render(request, "core/category_list.html", context)
