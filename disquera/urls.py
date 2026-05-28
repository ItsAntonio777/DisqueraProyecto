from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('category/<slug:slug>/', views.category_detail, name='category_detail'),

    path('detail/<int:id>/', views.detail, name='detail'),

    path('cart/', views.cart, name='cart'),

    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),

    path('register/', views.register, name='register'),

    path(
        'login/',
        auth_views.LoginView.as_view(template_name='disquera/login.html'),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path('checkout/', views.checkout, name='checkout'),

    path('success/', views.success, name='success'),

    path('my-orders/', views.my_orders, name='my_orders'),

    path('profile/', views.profile, name='profile'),

    path('search/', views.search, name='search'),

    path('cart/update/<int:id>/<str:action>/', views.update_cart_quantity, name='update_cart_quantity'),
]