"""
URL configuration for almurut_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from market.views import HomeView, FavoritesView, ProductListView, ProductDetailView, SendProductFeedbackView
from users.views import LoginView, UserRegistrationView, MakeUserRegistrationView, MakeUserLoginView, \
    MakeUserLogoutView, FaqView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home-url'),
    path('favorites/', FavoritesView.as_view()),
    path('login/', LoginView.as_view(), name='login-view'),
    path('make-login/', MakeUserLoginView.as_view(), name='make-login-url'),
    path('make-logout/', MakeUserLogoutView.as_view(), name='make-logout-url'),
    path('registration/', UserRegistrationView.as_view(), name='registration-url'),
    path('make-registration/', MakeUserRegistrationView.as_view(), name='make-registration-url'),
    path('faq/', FaqView.as_view(), name='faq-url'),
    path('products/', ProductListView.as_view(), name='product-list-url'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail-url'),
    path('products/<int:pk>/send-feedback/', SendProductFeedbackView.as_view(), name='send-feedback-url'),
    path('favorites/', FavoritesView.as_view(), name='favorites-url')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
