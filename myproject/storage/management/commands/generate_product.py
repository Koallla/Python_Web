from django.core.management.base import BaseCommand
from storage.models import Category, Product
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Create random Category and Products'

    def add_arguments(self, parser):
        parser.add_argument('category_count', type=int, help='Count of categories to be created')
        parser.add_argument('product_count', type=int, help='Count of products to be created')

    def handle(self, *args, **kwargs):
        category_count, product_count = kwargs['category_count'], kwargs['product_count']
        category_list = [Category(name=get_random_string(10)) for i in range(category_count)]
        Category.objects.bulk_create(category_list, batch_size=10000)
        self.stdout.write(f'Created {category_count} category')

        products_list = []
        for category_name in category_list:
            category = Category.objects.get(name=category_name)
            for idx in range(product_count):
                product_list = Product(name=get_random_string(6), category=category)
                products_list.append(product_list)
        
        Product.objects.bulk_create(products_list)
        self.stdout.write(f'Created {product_count * category_count} products')


