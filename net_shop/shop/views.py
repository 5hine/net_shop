from django.shortcuts import render, get_object_or_404
from .models import Product,ProductCategory
# Create your views here.


def index(request):
    all_category = ProductCategory.objects.all()
    product_category = []
    for everyone in all_category:
        # 每个类别 显示 两个
        product_category.append((everyone, Product.objects.filter(category=everyone)[:2]))
    # 字典虽然是发给index.html ，index 继承base  base 也可以用此字典
    content = {"category_product": product_category, "all_category": all_category}
    return render(request, 'shop/index.html', content)


def every_category(request, category_id):
    all_category = ProductCategory.objects.all()
    need_category = get_object_or_404(ProductCategory, id=category_id)
    product_category = [(need_category, Product.objects.filter(category=need_category)[:2])]
    content = {"category_product": product_category, "all_category": all_category}
    return render(request, 'shop/index.html', content)


def every_product(request, category_id, product_id):
    all_category = ProductCategory.objects.all()
    product = get_object_or_404(Product, id=product_id, is_on_shelf=True)
    # product_category = [(need_category, Product.objects.filter(category=need_category)[:2])]
    content = {"product": product, "all_category": all_category}
    return render(request, 'shop/detail.html', content)
