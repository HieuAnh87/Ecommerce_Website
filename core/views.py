from django.shortcuts import render
from core.models import Product, Category, CartOrder, CartOrderItems, ProductReviews, Wishlist, Address, ProductImages, \
    Vendor


# Homepage
def index(request):
    # products = Product.objects.all().order_by('-id')

    products = Product.objects.filter(featured=True, product_status='published').order_by('-id')
    context = {
        'products': products
    }
    return render(request, "core/index.html", context)


# Categories
def category_list_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, "core/category_list.html", context)


# Category Detail
def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(category=category, product_status='published').order_by('-id')
    context = {
        'products': products,
        'category': category
    }
    return render(request, "core/category_product_list.html", context)


# Vendors
def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {
        'vendors': vendors
    }
    return render(request, "core/vendor_list.html", context)


# Vendor Detail
def vendor_detail_view(request, vid):
    vendors = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendors, product_status='published').order_by('-id')
    context = {
        'vendors': vendors,
        'products': products
    }
    return render(request, "core/vendor_detail.html", context)


# Products
def product_list_view(request):
    products = Product.objects.filter(product_status='published').order_by('-id')
    context = {
        'products': products
    }
    return render(request, "core/product_list.html", context)


# Product Detail
def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    category = Category.objects.get(cid=product.category.cid)
    p_image = product.p_images.all()
    context = {
        'product': product,
        'category': category,
        'p_image': p_image,
    }
    return render(request, "core/product_detail.html", context)
