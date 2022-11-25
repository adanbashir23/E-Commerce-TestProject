from django.forms import inlineformset_factory

from .models import Cart, CartItem

CartFormSet = inlineformset_factory(
    Cart,
    CartItem,
    fields=('quantity', ),
    extra=0,
    can_delete=True
)
