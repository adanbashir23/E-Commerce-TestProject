# pylint: disable=E1101
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in
from django.db import transaction
from django.dispatch import receiver
from django.http import HttpResponseRedirect

# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from cart.forms import CartFormSet
from cart.models import Cart, CartItem
from products.models import Product

# from promocodes.models import Promocode


def view_cart(request):
    """View a cart"""
    # cart_object = {"cart": Cart.objects.get(user=request.user)}
    if request.method == "POST":
        formset = CartFormSet(request.POST, instance=request.cart)
        # promocode = request.POST.get("promocode")

        if formset.is_valid():
            formset.save()
            messages.success(request, "Your cart has been updated.")
            # if promocode:
            # promocode_object = Promocode.objects.filter(code__icontains=promocode)
            # cart_object.promocode = promocode_object
            # cart_object.save()
            # messages.success(request, "Coupon applied.")

            formset = CartFormSet(instance=request.cart)

            # messages.success(request, "Coupon applied.")
            # return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        else:
            messages.error(
                request,
                "Your cart could not be updated, please review any "
                "error messages below.",
            )

    else:
        if hasattr(request, "cart"):
            formset = CartFormSet(instance=request.cart)
        else:
            formset = None

    context = {"formset": formset}

    return render(request, "cart/cart.html", context)


# def cart(request):
#     cart_object = {"cart": Cart.objects.get(is_active=True, user=request.user)}
#     if request.method == "POST":
#         promocode = request.POST.get("promocode")
#         promocode_object = Promocode.objects.filter(code__icontains=promocode)

#         if not promocode_object.exists():
#             messages.warning(request, "Invalid Coupon.")
#             return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

#         if cart_object.promocode:
#             messages.warning(request, "Coupon already exists.")
#             return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

#         cart_object.promocode = promocode_object
#         cart_object.save()

#         messages.success(request, "Coupon applied.")
#         return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

#     context = {"cart": cart_object}
#     return render(request, "cart/cart.html", context)


@transaction.atomic
def add_to_cart(request, product_id):
    """add a new product to the cart"""
    product = get_object_or_404(Product, serial_number=product_id)

    if hasattr(request, "cart") and request.cart is not None:
        # cart already exists
        cart = request.cart
    else:
        # no cart in request object - this is a new cart
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None

        # create new cart and store in session var for accessing
        cart = Cart.objects.create(user=user)
        request.session["cart_id"] = cart.id

    # cart exists (otherwise raise 404), add or update cart item
    cart_item, new = CartItem.objects.get_or_create(cart=cart, product=product)

    if new:
        # new product in cart
        messages.success(request, f"{product.product_name} added to cart.")
    else:
        # product already exists
        # make sure that cart quantity does not exceed maximum amount
        if cart_item.quantity < 5:
            # update quantity
            cart_item.quantity += 1
            cart_item.save()
            messages.info(
                request,
                f"{product.product_name} quantity now \
                    {cart_item.quantity}.",
            )
        else:
            messages.warning(
                request,
                "You have the maximum permitted amount of this item \
                    in your cart, no more can be added.",
            )

    return redirect(reverse("cart"))


@receiver(user_logged_in)
def get_cart(sender, user, request, **kwargs):
    """When user logs in, retrieve cart and merge with existing"""

    try:
        # does the user have a cart already stored in db
        existing_cart = Cart.objects.get(user=user, status=Cart.IN_PROGRESS)

        # check to see if added any items to cart before logging in
        if hasattr(request, "cart"):
            new_items_cart = request.cart
            new_items = []

            try:
                # loop through new items and store as list of dictionaries
                for item in new_items_cart.cartitem_set.all():
                    new_items += [{"product": item.product, "quantity": item.quantity}]

                # check list against existing cart, add new, update existing
                for item in new_items:
                    cart_item, new = CartItem.objects.get_or_create(
                        cart=existing_cart, product=item["product"]
                    )

                    if new:
                        quantity = item["quantity"]
                    else:
                        # add existing quantity to new cart quantity
                        quantity = cart_item.quantity + item["quantity"]

                    # check quantity does not exceed maximum permissable amount
                    if quantity > 5:
                        quantity = 5
                        messages.warning(
                            request,
                            f"Product '{item['product']}' exceeded the \
                                maximum quantity, quantity set to maximum \
                                    permittable amount.",
                        )
                    # set quantity and save object
                    cart_item.quantity = quantity
                    cart_item.save()
            except Exception as e_c:
                # capture exceptions coming from no cart items
                print(e_c)
                pass

            # provide feedback to user
            messages.info(
                request,
                "Your new items have been merged with your existing \
                    cart.",
            )
            # remove anonymous cart, given contents merged into user cart
            new_items_cart.delete()

        # update session variable to enable middleware to set request.cart
        request.session["cart_id"] = existing_cart.id

    except Cart.DoesNotExist:
        # user account does not already have an 'in progress' cart
        # check to see if user created a cart anonymously
        # if so, attach it to the user's account
        cart_id = request.session.get("cart_id", False)

        if cart_id:
            try:
                cart = Cart.objects.get(id=request.session["cart_id"], user=None)

                if cart:
                    # cart exists, update user to current user
                    cart.user = user
                    cart.save()
            except Cart.DoesNotExist:
                # user does not have a cart
                pass
