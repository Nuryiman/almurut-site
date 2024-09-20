from datetime import datetime

from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView

from market.models import Product, ProductUserRating
from users.models import CustomUser


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


class ProductListView(ListView):
    template_name = 'product-list.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = {
            'product_list': Product.objects.all(),
            'now': datetime.now().date()
        }
        return context


class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'

    def get_context_data(self, **kwargs):
        try:
            product_pk = Product.objects.get(id=kwargs['pk'])
        except Product.DoesNotExist:
            raise Http404
        context = {
            'product': product_pk
        }
        return context


class SendProductFeedbackView(View):
    """Вью для сохранения отзыва пользователя для конкретного товара"""

    def post(self, request, *args, **kwargs):
        data = request.POST
        rating_value = data['rating_value']
        comment = data['comment']

        product = Product.objects.get(id=kwargs['pk'])
        user = request.user
        if user.is_authenticated:

            ProductUserRating.objects.create(
                product=product,
                user=user,
                rating=rating_value,
                comment=comment
            )

            return redirect(f"products/{product.id}/")
        else:
            return redirect("/login/")
