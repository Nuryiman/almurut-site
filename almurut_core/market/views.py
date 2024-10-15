from datetime import datetime

from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView

from market.models import Product, ProductUserRating


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


class ProductListView(ListView):
    template_name = 'product-list.html'
    queryset = Product.objects.all()
    model = Product
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Добавляем новые данные в контекст
        context['now'] = datetime.now().date()
        return context


class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'

    def get_context_data(self, **kwargs):
        five_range = [1, 2, 3, 4, 5]
        try:
            product = Product.objects.get(id=kwargs['pk'])
        except Product.DoesNotExist:
            raise Http404
        user = self.request.user
        try:
            if self.request.user.is_authenticated:
                my_rating = ProductUserRating.objects.get(user=user, product=product)
                my_rating = my_rating.rating if my_rating else 0
            else:
                my_rating = 0  # Если пользователь не авторизован, возвращаем 0
        except ProductUserRating.DoesNotExist:
            my_rating = 0

        product_rating_list = ProductUserRating.objects.filter(product=product)
        total_value = 0
        for product_rating in product_rating_list:
            total_value += product_rating.rating
        try:
            average_rating = total_value / len(product_rating_list)
        except ZeroDivisionError:
            average_rating = 0

        category_other_products = Product.objects.filter(category=product.category.id).exclude(id=product.id)

        context = {
            'product': product,
            'my_rating': my_rating,
            'range': five_range,
            'average_rating': average_rating,
            'now': datetime.now().date(),
            'other_products': category_other_products
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
            try:
                product_rating = ProductUserRating.objects.get(user=user, product=product)
            except ProductUserRating.DoesNotExist:
                ProductUserRating.objects.create(
                    product=product,
                    user=user,
                    rating=rating_value,
                    comment=comment
                )

                return redirect('product-detail-url', pk=product.id)

            product_rating.rating = rating_value
            product_rating.save()
            return redirect('product-detail-url', pk=product.id)
        else:
            return redirect("/login/")


class FavoritesView(TemplateView):
    """Показывает все избранные товары пользователя"""
    template_name = 'favorites.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            favorites = user.user_favorite_product.all()
            context = {
                'favorites': favorites
            }
            return context
        else:
            return render(self.request, "login.html", context={'logged_in': False})


class AddFavoriteView(TemplateView):
    """Вью для добавления товара в избранное"""
    template_name = "favorites.html"

    def get_context_data(self, **kwargs):
        product = Product.objects.get(id=kwargs['pk'])
        user = self.request.user
        user.user_favorite_product.add(product)
        user.save()
        favorites = user.user_favorite_product.all()
        context = {
            'favorites': favorites
        }
        return context


class RemoveFavoriteView(TemplateView):
    """Вью для добавления товара в избранное"""
    template_name = "favorites.html"

    def get_context_data(self, **kwargs):
        product = Product.objects.get(id=kwargs['pk'])
        user = self.request.user
        user.user_favorite_product.remove(product)
        user.save()
        favorites = user.user_favorite_product.all()
        context = {
            'favorites': favorites
        }
        return context
