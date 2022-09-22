from django.urls import path
from .views import cart_detail

urlpatterns = [
    path("cart/", cart_detail),
]
