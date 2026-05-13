from django.urls import path
from .views import home, detail

urlpatterns = [
    path('', home, name='home'),
    path('album/<int:id>/', detail, name='post_detail'),
]