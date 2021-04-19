from django.urls import path
from . import views

urlpatterns = [
    path("product", views.product),
    path("place_order", views.place_order)
]