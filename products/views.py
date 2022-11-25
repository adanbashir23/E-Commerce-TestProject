"""Product views"""
# pylint: disable=E1101

# Create models here
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
)

from .models import Product
# , ProductImage

class ProductListView(ListView):
    """List products from database with pagination"""

    model = Product
    queryset = Product.objects.get_queryset().order_by("product_name")
    #     rating=Avg('reviews__rating')).order_by('id')
    product_count = queryset.count()
    context = {"product_list": queryset, "product_count": product_count}
    template_name = "products/product_list.html"
    # paginate_by = 8


class ProductDetail(View):
    """Specify which view to be used dependent on request type"""

    def get(self, request, *args, **kwargs):
        view = ProductDetailView.as_view()
        return view(request, *args, **kwargs)


class ProductDetailView(DetailView):
    """Render output for a single product and enable review capture"""

    queryset = Product.objects.all()
    template_name = "products/product_detail.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    # PermissionRequiredMixin,
    """Authorized users can add new products"""
    # permission_required = 'products.add_product'
    model = Product
    fields = [
        "product_name",
        "product_brand",
        "category",
        "price",
        "stock",
        "description",
        "images",
    ]
    template_name = "products/product_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def upload(self, request):
    #     if request.method == "POST":
    #         images = request.FILES.getlist("images")
    #         for image in images:
    #             Product.objects.create(images=image)
    #     images = Product.objects.all()
    #     return render(request, "product_detail.html", {"images": images})


class ProductDeleteView(DeleteView):
    """Authorized users can delete products"""

    # permission_required = 'products.delete_product'
    model = Product
    context_object_name = "product"
    template_name = "products/product_delete.html"
    success_url = reverse_lazy("product_list")


class ProductUpdateView(UpdateView):
    """Authorized users can update all product fields"""

    # permission_required = 'products.change_product'
    model = Product
    fields = [
        "product_name",
        "product_brand",
        "category",
        "price",
        "stock",
        "description",
        "images",
    ]
    context_object_name = "product"
    template_name = "products/product_update.html"
