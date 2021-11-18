"""djreactshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .yasg import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from eshop.views import index, category_detail, add_to_cart, cart_detail, order_detail, ProductDetail, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('eshop_api.urls')),
    path('', index),
    path('cart_detail/', cart_detail),
    path('order/', order_detail),
    path('login/', login),
    path('auth', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('api/v1/auth_token/', include('djoser.urls.authtoken')),
    path('product/<int:id>/', ProductDetail.as_view()),
    path('category/<int:id>/', category_detail),
    path('current_customer_cart/add_to_cart/<str:id>/', add_to_cart),
    # JWT auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
urlpatterns += urlpatterns_yasg
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
