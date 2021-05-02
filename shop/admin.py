from django.contrib import admin
from .models import Cart, Product, CartProduct, Category, Order, Favorite


admin.site.register([Cart, Product, CartProduct, Category, Order, Favorite, ])
