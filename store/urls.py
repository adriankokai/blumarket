from django.urls import path
from . import views

urlpatterns = [
    path("product/<int:id>/", views.product),
    path("place_order/", views.place_order),
    path("products/", views.products)
]