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
from market.views import HomeView, FavoritesView
from users.views import LoginView, UserRegistrationView, MakeUserRegistrationView, MakeUserLoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view()),
    path('favorites/', FavoritesView.as_view()),
    path('login/', LoginView.as_view(), name='login-view'),
    path('make-login/', MakeUserLoginView.as_view(), name='make-login-url'),
    path('registration/', UserRegistrationView.as_view(), name='registration-url'),
    path('make-registration/', MakeUserRegistrationView.as_view(), name='make-registration-url')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
