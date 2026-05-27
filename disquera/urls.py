from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    home,
    detail,
    cart,
    add_to_cart,
    register,
    checkout,
    success,
    my_orders,
    category_detail
)

urlpatterns = [
    path(
    'category/<slug:slug>/',
    category_detail,
    name='category_detail'
),

    path('', home, name='home'),

    path('detail/<int:id>/', detail, name='detail'),

    path('cart/', cart, name='cart'),

    path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),

    path('register/', register, name='register'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='disquera/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path('checkout/', checkout, name='checkout'),

    path('success/', success, name='success'),

    path('my-orders/', my_orders, name='my_orders'),
]