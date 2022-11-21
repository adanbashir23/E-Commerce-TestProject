from django.urls import reverse
from django.shortcuts import redirect


class CartNotEmptyMixin:
    """Prevent user from accessing view if cart is empty"""

    def dispatch(self, request, *args, **kwargs):
        # check cart is part of request object
        if hasattr(self.request, 'cart'):
            cart = self.request.cart
        else:
            cart = None
        # make sure the user's cart is not empty
        if not cart or cart.count() == 0:
            return redirect(reverse('cart'))

        return super().dispatch(request, *args, **kwargs)
