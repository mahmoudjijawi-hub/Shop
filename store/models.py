from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='الاسم')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='الرابط')
    description = models.TextField(blank=True, verbose_name='الوصف')
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name='الصورة')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'فئة'
        verbose_name_plural = 'الفئات'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:category_detail', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE, verbose_name='الفئة'
    )
    name = models.CharField(max_length=200, verbose_name='الاسم')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='الرابط')
    description = models.TextField(verbose_name='الوصف')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='السعر')
    stock = models.PositiveIntegerField(default=0, verbose_name='المخزون')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='الصورة')
    available = models.BooleanField(default=True, verbose_name='متاح')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'منتج'
        verbose_name_plural = 'المنتجات'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    @property
    def in_stock(self):
        return self.stock > 0 and self.available
