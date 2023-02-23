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
