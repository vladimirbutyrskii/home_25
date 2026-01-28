from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView
from catalog.models import Product


class ProductListView(ListView):
    model = Product

    # app_name/<model_name>_<action>  -  правило формирования названия шаблона
    # catalog/product_list.html


# def products_list(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'catalog/products_list.html', context)

class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'catalog/products_detail.html', context)
