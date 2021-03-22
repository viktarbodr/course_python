from django.urls import path
from django.contrib.auth import views
from cart import views


app_name = 'cart'

urlpatterns = [
  #  path('view-cart/', views.CartView.as_view(), name='view-cart'),
    path('update-cart/', views.UpdateCart.as_view(), name='update-cart'),
    path('add-to-cart/', views.AddToCartView.as_view(), name='add-to-cart'),
]