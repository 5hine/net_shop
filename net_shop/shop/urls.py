from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path('', views.index, name='总览页'),
    # 动态获取 类别id
    path('<category_id>', views.every_category, name='单类页'),
    path('<category_id>/<product_id>', views.every_product, name='详情页'),
]
