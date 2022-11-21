from django.contrib import admin

from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


class CartAdmin(admin.ModelAdmin):
    list_display = ("account_identifier", "status", "item_count")
    list_display_links = ("account_identifier",)
    list_editable = ("status",)
    list_filter = ("status",)

    inlines = [
        CartItemInline,
    ]

    def account_identifier(self, obj):
        """Return user field"""
        if obj.user is None:
            identifier = "Anonymous"
        else:
            identifier = obj.user.email

        return identifier

    def item_count(self, obj):
        """Return item count"""
        return obj.count()

    # relabel admin list column headers
    account_identifier.short_description = "Account"
    item_count.short_description = "Items in Cart"


admin.site.register(Cart, CartAdmin)
