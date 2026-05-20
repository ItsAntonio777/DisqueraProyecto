from django.urls import path


from .views import (
    home,
    detail,
    cart,
    add_to_cart
)


urlpatterns = [


    path(
        '',
        home,
        name='home'
    ),


    path(
        'detail/<int:id>/',
        detail,
        name='detail'
    ),


    path(
        'cart/',
        cart,
        name='cart'
    ),


    path(
        'add-to-cart/<int:id>/',
        add_to_cart,
        name='add_to_cart'
    ),
]
