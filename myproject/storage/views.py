from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Product


def index(request):
    return HttpResponse("Hello, world!")


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def products_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    # categories = [{'da': 1}, {'dad': 2}]
    context = {'products': products}
    return render(request, 'storage/products.html', context)