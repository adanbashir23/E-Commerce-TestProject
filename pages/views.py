# pylint: disable=E1101
from django.db.models import Count
from django.views.generic import TemplateView

from products.models import Product

# Create your views here.


class HomePageView(TemplateView):
    """Show most popular and newest products to end-user"""

    template_name = "pages/homepage.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # get top 5 sellers
        context["products"] = Product.objects.annotate(
            items_sold=Count("orderitem")
        ).order_by("-items_sold")[:5]
        # get the last 5 products added
        return context
