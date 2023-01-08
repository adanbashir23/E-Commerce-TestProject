"""Product admin"""
from django.contrib import admin

# Register your models here.
from .models import Promocode

admin.site.register(Promocode)

# from .models import Product, ProductImage

# class ProductImageAdmin(admin.StackedInline):
#     model = ProductImage

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ProductImageAdmin]

#     class Meta:
#        model = Product

# @admin.register(ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
#     pass


# class CommentInline(admin.TabularInline):
#     """Tabular Inline View for Product Reviews"""

#     model = Comment


# class ProductAdmin(admin.ModelAdmin):
#     """Update view for admin panel"""

#     def has_change_permission(request, obj=None, user):
#         product = request.product
#         if request.user == product.user:
#             return True
#         else:
#             return False
#         # Should return True if editing obj is permitted, False otherwise.
#         # If obj is None, should return True or False to indicate whether editing of objects of this type is permitted in general


# admin.site.register(Product,ProductAdmin)
