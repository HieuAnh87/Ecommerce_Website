from django.urls import path
from core.views import index, product_list_view, category_list_view, category_product_list_view, vendor_list_view, \
    vendor_detail_view

app_name = "core"

urlpatterns = [
    # Homepage
    path("", index, name="index"),
    # Product
    path("products/", product_list_view, name="product_list"),
    # Category
    path("categories/", category_list_view, name="category_list"),
    # Category Detail
    path("categories/<cid>/", category_product_list_view, name="category_product_list"),
    # Vendor
    path("vendors/", vendor_list_view, name="vendor_list"),
    # Vendor Detail
    path("vendors/<vid>/", vendor_detail_view, name="vendor_detail"),

]
