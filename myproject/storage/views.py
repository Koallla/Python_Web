from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View

from .models import Category, Product



class MyView(View):
    def get(self, request):
        products_list = Product.objects.all()
        paginator = Paginator(products_list, 50)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'storage/products.html', {'page_obj': page_obj})