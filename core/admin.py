from django.contrib import admin
from core.models import Product, Category, CartOrder, CartOrderItems, ProductReviews, Wishlist, Address, ProductImages, \
    Vendor


# from import_export.admin import ImportExportModelAdmin

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid', 'user', 'title', 'product_image', 'price', 'category', 'vendor', 'featured',
                    'product_status', 'date']
    inlines = [ProductImagesAdmin]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']


class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']


class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'paid_status', 'order_date', 'product_status']


class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice_no', 'product_status', 'item', 'image', 'qty', 'price', 'total']


class ProductReviewsAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating', 'date']


class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'status']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(ProductReviews, ProductReviewsAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)
