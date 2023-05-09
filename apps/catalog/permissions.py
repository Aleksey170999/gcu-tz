from django.shortcuts import get_object_or_404, redirect
from .models import Category, Product


def check_category_manager(view_func):
    def wrapped_view(request, cat_uid, *args, **kwargs):
        category = get_object_or_404(Category, uid=cat_uid)
        if request.user.is_superuser:
            return view_func(request, cat_uid, *args, **kwargs)
        if category.manager != request.user:
            return redirect('catalog:access_denied')  # Перенаправить на страницу отказа в доступе
        return view_func(request, cat_uid, *args, **kwargs)

    return wrapped_view


def check_product_manager(view_func):
    def wrapped_view(request, prod_uid, *args, **kwargs):
        product = get_object_or_404(Product, uid=prod_uid)
        if request.user.is_superuser:
            return view_func(request, prod_uid, *args, **kwargs)
        if product.category.manager != request.user:
            return redirect('catalog:access_denied')  # Перенаправить на страницу отказа в доступе
        return view_func(request, prod_uid, *args, **kwargs)

    return wrapped_view