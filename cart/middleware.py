# pylint: disable=E1101
from .models import Cart


class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # check that a cart session exists
        cart_id = request.session.get("cart_id", False)

        try:
            if cart_id:
                # if session variable exists, store cart object in request
                # object to access from any view
                request.cart = Cart.objects.get(id=cart_id, status=Cart.IN_PROGRESS)
            else:
                # make sure user is logged in
                if request.user.is_authenticated:
                    # no session variable, check if user has cart in db
                    # store in request object
                    request.cart = Cart.objects.get(
                        user=request.user, status=Cart.IN_PROGRESS
                    )
        except Cart.DoesNotExist:
            # cart not in db, unset variables
            request.session["cart_id"] = None
            request.cart = None

        response = self.get_response(request)

        return response
