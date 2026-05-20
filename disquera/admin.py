# disquera/admin.py/javier 


from django.contrib import admin


from .models import (
    Category,
    Artist,
    Post,
    Specification,
    Comment,
    CartItem
)


admin.site.register(Category)


admin.site.register(Artist)


admin.site.register(Post)


admin.site.register(Specification)


admin.site.register(Comment)


admin.site.register(CartItem)

