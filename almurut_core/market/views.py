from datetime import datetime

from django.shortcuts import render
from django.views.generic import TemplateView

from market.models import Product


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        all_products = Product.objects.all()
        first_product = Product.objects.first()
        context = {
            "all_products": all_products,
            "product": first_product
        }
        return context


class FavoritesView(TemplateView):
    template_name = 'favorites.html'


class ProductListView(TemplateView):
    template_name = 'product-list.html'

    def get_context_data(self, **kwargs):
        context = {
            'product_list': Product.objects.all(),
            'now': datetime.now().date()
        }
        return context
