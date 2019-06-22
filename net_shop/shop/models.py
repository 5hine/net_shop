from django.db import models

# Create your models here.
from datetime import datetime


class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="名称")
    describe = models.TextField(blank=True, verbose_name="描述")
    image = models.ImageField(upload_to='category', blank=True, verbose_name="图片")#

    # 用于admin 站点 显示 名称
    class Meta:
        verbose_name = "商品类别表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="名称")
    describe = models.TextField(blank=True, verbose_name="描述")
    image = models.ImageField(upload_to='category', blank=True, verbose_name="图片")
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,
                                 verbose_name="商品类别")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="价格")
    reserve = models.IntegerField(default=0, verbose_name="库存")
    is_on_shelf = models.BooleanField(default=True, verbose_name="已上架")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    modify_time = models.DateTimeField(default=datetime.now, verbose_name="修改时间")

    class Meta:
        verbose_name = "商品表"
        verbose_name_plural = verbose_name
        ordering = ("-add_time",)

    def __str__(self):
        return self.name
