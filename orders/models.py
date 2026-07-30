from django.db import models
from django.contrib.auth.models import User
from store.models import Product


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد الانتظار'),
        ('processing', 'قيد المعالجة'),
        ('shipped', 'تم الشحن'),
        ('delivered', 'تم التسليم'),
        ('cancelled', 'ملغي'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders', verbose_name='المستخدم'
    )
    first_name = models.CharField(max_length=100, verbose_name='الاسم الأول')
    last_name = models.CharField(max_length=100, verbose_name='الاسم الأخير')
    email = models.EmailField(verbose_name='البريد الإلكتروني')
    phone = models.CharField(max_length=20, verbose_name='الهاتف')
    address = models.CharField(max_length=250, verbose_name='العنوان')
    city = models.CharField(max_length=100, verbose_name='المدينة')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='المجموع')
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='الحالة'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'طلب'
        verbose_name_plural = 'الطلبات'
        ordering = ['-created_at']

    def __str__(self):
        return f'طلب #{self.id} - {self.user.username}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='السعر')
    quantity = models.PositiveIntegerField(default=1, verbose_name='الكمية')

    class Meta:
        verbose_name = 'عنصر الطلب'
        verbose_name_plural = 'عناصر الطلب'

    def __str__(self):
        return f'{self.quantity}x {self.product.name}'

    @property
    def subtotal(self):
        return self.price * self.quantity
