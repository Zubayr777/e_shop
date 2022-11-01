from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    # path('products', views.get_all_products),
    # path('categories', views.categories),
    path('search', views.search_exact_product),
    path('product/<str:pk>', views.get_exact_product),
    path('category/<str:pk>', views.get_exact_category),
    path('add_to_cart/<str:pk>', views.add_product_to_user_cart),
    path('cart', views.user_cart),
    path('zakaz', views.zakaz),
    path('delete_product/<str:pk>', views.delete_exact_user_cart)
]