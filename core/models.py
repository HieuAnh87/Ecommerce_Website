from django.db import models
from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField
from userauths.models import User

STATUS_CHOICE = (
    ("process", "Processing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered"),
)

STATUS = (
    ("draft", "Draft"),
    ("disable", "Disable"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("published", "Published"),
)

RATING = (
    (1, "⭐☆☆☆☆"),
    (2, "⭐⭐☆☆☆"),
    (3, "⭐⭐⭐☆☆"),
    (4, "⭐⭐⭐⭐☆"),
    (5, "⭐⭐⭐⭐⭐"),
)


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Vendor(models.Model):
    # Using shortuuidfield to generate a short unique id
    # prefix is used to identify the model: In this model is 'ven'
    vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='ven',
                         alphabet="abcdefgh12345")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path)
    cover_image = models.ImageField(upload_to=user_directory_path, default='vendor-header-bg.png')
    description = models.TextField(null=True, blank=True)

    address = models.CharField(max_length=100, default='123 Street')
    contact = models.CharField(max_length=100, default='0123456789')
    chat_resp_time = models.CharField(max_length=100, default='100')
    shipping_on_time = models.CharField(max_length=100, default='100')
    authentic_rating = models.CharField(max_length=100, default='100')
    days_return = models.CharField(max_length=100, default='100')
    warranty_period = models.CharField(max_length=100, default='100')
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # Using ForeignKey to link to User model,
    # on_delete=models.SET_NULL means if the user is deleted, the vendor will be set to null instead of deleting
    # because user can have many vendors, but a vendor can only have one user
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Vendors'

    def vendor_image(self):
        if self.image:
            return mark_safe('<img src="%s" width="50" height="50" />' % self.image.url)
        else:
            return 'No Image Found'

    def __str__(self):
        return self.title


class Category(models.Model):
    # Using shortuuidfield to generate a short unique id
    # prefix is used to identify the model: In this model is 'cat'
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='cat',
                         alphabet="abcdefgh12345")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category', blank=True, null=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def category_image(self):
        if self.image:
            return mark_safe('<img src="%s" width="50" height="50" />' % self.image.url)
        else:
            return 'No Image Found'

    def __str__(self):
        return self.title


# class Tags(models.Model):
#     pass


class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='prd', alphabet="abcdefgh12345")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, related_name="vendor")

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path)
    description = models.TextField(null=True, blank=True, default='This is the product')

    price = models.DecimalField(max_digits=99999999999999, decimal_places=2, default="1.99")
    old_price = models.DecimalField(max_digits=999999999999, decimal_places=2, default="1.99")

    specifications = models.TextField(null=True, blank=True, default='This is the product')
    type = models.CharField(max_length=100, default='This is the product')
    stock_count = models.CharField(max_length=100, default='8')
    life = models.CharField(max_length=100, default='100 Days')
    mfd = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    # tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)

    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")

    status = models.BooleanField(default=True)  # active or not
    in_stock = models.BooleanField(default=True)  # in stock or not
    featured = models.BooleanField(default=False)  # featured product
    digital = models.BooleanField(default=False)  # digital product

    sku = ShortUUIDField(unique=True, length=5, max_length=10, prefix='sku', alphabet="1234567890")

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Products'

    def product_image(self):
        if self.image:
            return mark_safe('<img src="%s" width="50" height="50" />' % self.image.url)
        else:
            return 'No Image Found'

    def __str__(self):
        return self.title

    def get_percentage(self):
        new_price = ((self.old_price - self.price) / self.old_price) * 100
        return int(new_price)


class ProductImages(models.Model):
    image = models.ImageField(upload_to="product-images", default="product.png")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="p_images")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Images'


########################################## CART, ORDER, ORDERITEMS and ADDRESS ##################################
########################################## CART, ORDER, ORDERITEMS and ADDRESS ##################################
########################################## CART, ORDER, ORDERITEMS and ADDRESS ##################################

class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=999999999999, decimal_places=2, default="1.99")
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="prrocessing")

    class Meta:
        verbose_name_plural = 'Cart Orders'


class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=999999999999, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=999999999999, decimal_places=2, default=0.00)

    class Meta:
        verbose_name_plural = 'Cart Order Items'

    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % self.image)


########################################## Product Review, Wishlist, Address ##################################
########################################## Product Review, Wishlist, Address ##################################
########################################## Product Review, Wishlist, Address ##################################

class ProductReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Reviews'

    def __str__(self):
        return self.product.title

    def get_rating(self):
        return self.rating


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Wishlists'

    def __str__(self):
        return self.product.title


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Addresses'
