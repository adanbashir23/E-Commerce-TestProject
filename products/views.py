# pylint: disable=E1101

# Create models here
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
# from django.db.models import Q, Avg
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View

from .models import Product, ProductImage

# class ProductListView(ListView):
#     """List products from database with pagination"""
#     model = Product
#     context_object_name = 'product_list'
#     # queryset = Product.objects.get_queryset().annotate(
#     #     rating=Avg('reviews__rating')).order_by('id')
#     template_name = 'products/product_list.html'
#     paginate_by = 8

class ProductDetail(View):
    """Specify which view to be used dependent on request type"""

    def get(self, request, *args, **kwargs):
        view = ProductDetailView.as_view()
        return view(request, *args, **kwargs)


class ProductDetailView(DetailView):
    """Render output for a single product and enable review capture"""
    queryset = Product.objects.all()
    # product = get_object_or_404(Product, serial_number=serial_number)
    # photos = ProductImage.objects.filter(product=product)
    template_name = 'products/product_detail.html'

class ProductCreateView(LoginRequiredMixin,CreateView):
    # PermissionRequiredMixin,
    """Authorized users can add new products"""
    # permission_required = 'products.add_product'
    model = Product
    fields = ['product_name','product_brand', 'category','price','stock','description', 'image']
    template_name = 'products/product_create.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

