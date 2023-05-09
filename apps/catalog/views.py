from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from apps.catalog.forms import ProductCreateForm, CategoryCreateForm
from apps.catalog.models import Category, Product
from apps.catalog.permissions import check_category_manager, check_product_manager

User = get_user_model()


@login_required
def category_list(request, *args, **kwargs):
    user = User.objects.get(username=request.user.username)
    if user.is_staff:
        categories = Category.objects.all()
        context = {'categories': categories,
                   'user': request.user}
    elif user.is_manager:
        user = User.objects.get(username=request.user.username)
        categories = Category.objects.filter(is_active=True, manager=user)
        context = {'categories': categories,
                   'user': request.user}
    else:
        context = {'user': request.user}
    return render(request, 'catalog/category-list.html', context)


@login_required
@check_category_manager
def products_by_cat_uid(request, cat_uid):
    category = Category.objects.get(uid=cat_uid)
    products = Product.objects.filter(category=category)
    context = {'products': products,
               'category': category}
    return render(request, 'catalog/product-list.html', context)


@login_required
@check_product_manager
def product_detail_by_uid(request, prod_uid):
    product = Product.objects.get(uid=prod_uid)
    context = {'product': product}
    return render(request, 'catalog/product-detail.html', context)


@login_required
@check_category_manager
def product_create(request, cat_uid):
    category = Category.objects.get(uid=cat_uid)

    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            product = Product()
            product.title = form.cleaned_data['title']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.category = category
            product.save()
            return redirect("catalog:category_list")
    else:
        form = ProductCreateForm()
        context = {'category': category,
                   'product_form': form}
        return render(request, 'catalog/product-create.html', context)


@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            category = form.save()
            category.title = form.cleaned_data['title']
            category.save()
            return redirect("catalog:category_list")
    else:
        form = CategoryCreateForm()
        context = {'category_form': form}
        return render(request, 'catalog/category-create.html', context)


@login_required
def search_results(request):
    query = request.GET.get("q")
    or_lookup = (Q(title__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query))

    products = Product.objects.filter(or_lookup)
    context = {'products': products}
    return render(request, 'catalog/search-results.html', context)


@login_required
@check_product_manager
def product_edit(request, prod_uid):
    product = get_object_or_404(Product, uid=prod_uid)

    if request.method == 'GET':
        form = ProductCreateForm(instance=product)

    if request.method == 'POST':
        form = ProductCreateForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('catalog:product_detail', prod_uid=prod_uid)

    return render(request, 'catalog/product_edit.html', {'product_form': form, 'product': product})


@login_required
def access_denied(request):
    return render(request, 'catalog/access-denied.html')
