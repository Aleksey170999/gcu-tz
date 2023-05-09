from django.urls import path, include

from apps.catalog.views import (access_denied,
                                products_by_cat_uid,
                                product_detail_by_uid,
                                product_create,
                                category_create,
                                search_results,
                                product_edit,
                                category_list)

app_name = 'catalog'

urlpatterns = [
    path('', category_list, name='category_list'),
    path('access_denied/', access_denied, name='access_denied'),
    path('search/', search_results, name='search_results'),
    path('create_category/', category_create, name='category_create'),
    path('detail/<str:prod_uid>/', product_detail_by_uid, name='product_detail'),
    path('product_edit/<str:prod_uid>/', product_edit, name='product_edit'),
    path('<str:cat_uid>/', products_by_cat_uid, name='product_list'),
    path('<str:cat_uid>/create/', product_create, name='product_create'),
]
