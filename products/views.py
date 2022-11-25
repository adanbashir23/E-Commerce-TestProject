"""Product views"""
# pylint: disable=E1101

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

# Create models here
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    ListView,
    UpdateView,
    View,
)

from .forms import CommentForm
from .models import Comment, Product

# , ProductImage


class ProductListView(ListView):
    """List products from database with pagination"""

    model = Product
    queryset = Product.objects.get_queryset().order_by("product_name")
    #     rating=Avg('comments__rating')).order_by('id')
    product_count = queryset.count()
    context = {"product_list": queryset, "product_count": product_count}
    template_name = "products/product_list.html"
    paginate_by = 2


class ProductDetail(View):
    """Specify which view to be used dependent on request type"""

    def get(self, request, *args, **kwargs):
        """get product details"""
        view = ProductDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Post comment to product"""
        view = ProductComment.as_view()
        return view(request, *args, **kwargs)


class ProductDetailView(DetailView):
    """Render output for a single product and enable comment capture"""

    queryset = Product.objects.all()
    template_name = "products/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # make sure the user is logged in first
        if self.request.user.is_authenticated:
            # check to see if user has already posted review for product
            user_has_reviewed = Comment.objects.filter(product=self.object).filter(
                user=self.request.user
            )
            # if no object was returned then user has not submitted a review
            if not user_has_reviewed:
                context["display_form"] = True

        # passthrough form for rendering in template
        context["form"] = CommentForm()

        return context


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


class ProductComment(FormView):
    """Displayed on product detail, used to add comments"""

    template_name = "products/product_detail.html"
    form_class = CommentForm
    model = Comment

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        form = self.form_class(request.POST)

        # store the product id passed through the url(defined as pk in urls.py)
        self.pk = kwargs.get("pk")

        if form.is_valid():
            # foreign key objects not yet added, prevent saving and add them
            comment = form.save(commit=False)
            comment.product = get_object_or_404(Product, pk=self.pk)
            comment.user = self.request.user
            comment.save()
        else:
            return self.form_invalid(form)

        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})


class ProductSearchResultsView(ListView):
    """Return products that match search query"""

    model = Product
    context_object_name = "search_results"
    # to avoid inconsistent pagination results order by id
    template_name = "products/product_search.html"
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        """Filter for search terms"""
        queryset = super().get_queryset()

        keywords = self.request.GET.get("keywords")
        if keywords:
            # filter data for anything that contains the kws
            # use the django Q object to create equivalent of SQL 'OR' query
            return queryset.filter(
                Q(product_name__icontains=keywords)
                | Q(product_brand__icontains=keywords)
                | Q(category__icontains=keywords)
                | Q(description__icontains=keywords)
            ).order_by("product_name")
        else:
            return ""

    def get_context_data(self, *, object_list=None, **kwargs):
        """Pass through the search terms to autopopulate search box"""
        context = super().get_context_data(**kwargs)
        # store search term in results to populate template search box
        context["search_keywords"] = self.request.GET.get("keywords")
        return context
