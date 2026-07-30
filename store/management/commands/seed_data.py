from django.core.management.base import BaseCommand
from store.models import Category, Product


class Command(BaseCommand):
    help = 'إنشاء بيانات تجريبية للمتجر'

    def handle(self, *args, **options):
        categories_data = [
            {
                'name': 'إلكترونيات',
                'slug': 'electronics',
                'description': 'أجهزة إلكترونية ومستلزماتها',
            },
            {
                'name': 'ملابس',
                'slug': 'clothing',
                'description': 'أزياء وملابس رجالية ونسائية',
            },
            {
                'name': 'كتب',
                'slug': 'books',
                'description': 'كتب ومجلات ومراجع',
            },
            {
                'name': 'رياضة',
                'slug': 'sports',
                'description': 'معدات وأدوات رياضية',
            },
            {
                'name': 'منزل',
                'slug': 'home',
                'description': 'مستلزمات المنزل والديكور',
            },
            {
                'name': 'جمال',
                'slug': 'beauty',
                'description': 'منتجات العناية والجمال',
            },
        ]

        products_data = [
            {
                'category': 'electronics',
                'name': 'سماعات بلوتوث',
                'slug': 'bluetooth-headphones',
                'description': 'سماعات بلوتوث عالية الجودة مع إلغاء الضوضاء وعمر بطارية يصل إلى 30 ساعة.',
                'price': 299.99,
                'stock': 50,
            },
            {
                'category': 'electronics',
                'name': 'شاحن لاسلكي',
                'slug': 'wireless-charger',
                'description': 'شاحن لاسلكي سريع متوافق مع جميع الأجهزة التي تدعم الشحن اللاسلكي.',
                'price': 89.99,
                'stock': 100,
            },
            {
                'category': 'electronics',
                'name': 'كاميرا ويب HD',
                'slug': 'hd-webcam',
                'description': 'كاميرا ويب بدقة 1080p مع ميكروفون مدمج للمكالمات والبث المباشر.',
                'price': 199.99,
                'stock': 30,
            },
            {
                'category': 'clothing',
                'name': 'قميص قطني',
                'slug': 'cotton-shirt',
                'description': 'قميص قطني 100% مريح ومناسب للاستخدام اليومي بألوان متعددة.',
                'price': 79.99,
                'stock': 80,
            },
            {
                'category': 'clothing',
                'name': 'جينز كلاسيكي',
                'slug': 'classic-jeans',
                'description': 'بنطال جينز كلاسيكي بقصة مريحة وجودة عالية.',
                'price': 149.99,
                'stock': 60,
            },
            {
                'category': 'books',
                'name': 'تعلم البرمجة',
                'slug': 'learn-programming',
                'description': 'كتاب شامل لتعلم البرمجة من الصفر حتى الاحتراف مع أمثلة عملية.',
                'price': 59.99,
                'stock': 40,
            },
            {
                'category': 'books',
                'name': 'رواية عالمية',
                'slug': 'world-novel',
                'description': 'رواية مشوقة من الأدب العالمي مترجمة بأسلوب سلس وممتع.',
                'price': 45.99,
                'stock': 35,
            },
            {
                'category': 'sports',
                'name': 'حذاء رياضي',
                'slug': 'sports-shoes',
                'description': 'حذاء رياضي مريح للجري والتمارين اليومية مع تصميم عصري.',
                'price': 249.99,
                'stock': 45,
            },
            {
                'category': 'sports',
                'name': 'مجموعة أوزان',
                'slug': 'dumbbell-set',
                'description': 'مجموعة أوزان حديدية قابلة للتعديل من 2 إلى 20 كجم.',
                'price': 399.99,
                'stock': 20,
            },
            {
                'category': 'home',
                'name': 'مصباح LED',
                'slug': 'led-lamp',
                'description': 'مصباح LED ذكي بإضاءة قابلة للتعديل وتحكم عبر التطبيق.',
                'price': 129.99,
                'stock': 55,
            },
            {
                'category': 'home',
                'name': 'مجموعة أكواب',
                'slug': 'cup-set',
                'description': 'مجموعة 6 أكواب سيراميك بتصميم عصري وألوان متناسقة.',
                'price': 69.99,
                'stock': 70,
            },
            {
                'category': 'beauty',
                'name': 'كريم مرطب',
                'slug': 'moisturizing-cream',
                'description': 'كريم مرطب للوجه بمكونات طبيعية مناسب لجميع أنواع البشرة.',
                'price': 89.99,
                'stock': 90,
            },
            {
                'category': 'beauty',
                'name': 'عطر فاخر',
                'slug': 'luxury-perfume',
                'description': 'عطر فاخر برائحة مميزة تدوم طويلاً بحجم 100 مل.',
                'price': 349.99,
                'stock': 25,
            },
            {
                'category': 'electronics',
                'name': 'ماوس لاسلكي',
                'slug': 'wireless-mouse',
                'description': 'ماوس لاسلكي مريح بتصميم إرغونومي واتصال بلوتوث.',
                'price': 69.99,
                'stock': 75,
            },
            {
                'category': 'clothing',
                'name': 'معطف شتوي',
                'slug': 'winter-jacket',
                'description': 'معطف شتوي دافئ ومقاوم للماء بتصميم عصري.',
                'price': 299.99,
                'stock': 30,
            },
        ]

        for cat_data in categories_data:
            Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data,
            )

        for prod_data in products_data:
            category = Category.objects.get(slug=prod_data['category'])
            Product.objects.get_or_create(
                slug=prod_data['slug'],
                defaults={
                    'category': category,
                    'name': prod_data['name'],
                    'description': prod_data['description'],
                    'price': prod_data['price'],
                    'stock': prod_data['stock'],
                    'available': True,
                },
            )

        self.stdout.write(self.style.SUCCESS(
            f'تم إنشاء {Category.objects.count()} فئات و {Product.objects.count()} منتجات بنجاح!'
        ))
