from core.models import Category, Address


def default(request):
    categories = Category.objects.all()
    address = Address.objects.filter(user=request.user)
    return {
        'categories': categories,
        'address': address
    }
