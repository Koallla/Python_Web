from django.core.management.base import BaseCommand
from storage.models import Category, Product
from random import randint

class Command(BaseCommand):
    help = 'Create random data in Products'


    def __random_int(self, min, max):
        return randint(min, max) 


    def handle(self, *args, **kwargs):
        
        # За один запрос, для всех одинаковые значения
        # radom_price = self.__random_int(1, 1000000)
        # random_status = Product.CHOISES[self.__random_int(0, 1)][0]
        # random_remains = self.__random_int(1, 1000)
        # Product.objects.all().update(price=radom_price, status=random_status, remains=random_remains)


        # Для каждого
        products = Product.objects.all()
        for product in products:
            radom_price = self.__random_int(1, 1000000)
            random_status = Product.CHOISES[self.__random_int(0, 1)][0]
            random_remains = self.__random_int(1, 1000)
            product.price = radom_price
            product.status = random_status
            product.remains = random_remains
            product.save()



    