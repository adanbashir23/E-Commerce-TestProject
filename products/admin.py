from django.contrib import admin

from .models import Comment, Product

# Register your models here.
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


class CommentInline(admin.TabularInline):
    """Tabular Inline View for Product Reviews"""

    model = Comment


class ProductAdmin(admin.ModelAdmin):
    """Update view for admin panel"""

    list_display = ("product_name", "product_brand", "category", "price")
    list_filter = ("product_brand",)

    inlines = [
        CommentInline,
    ]


admin.site.register(Product, ProductAdmin)
