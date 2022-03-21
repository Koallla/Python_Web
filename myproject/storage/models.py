from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CHOISES = (('in_stock', 'In stock'), ('out_of_stock', 'Out of stock'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=12, choices=CHOISES, default='out_of_stock')
    remains = models.IntegerField(default=0)
    
    def __str__(self):
        return f'ID: {self.id} - {self.category} / {self.name} / {self.price} / {self.status} / {self.remains}'


