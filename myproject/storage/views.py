from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View

from .models import Product


class MyView(View):

    def get(self, request):
        products = Product.objects.all().order_by('id')
        paginator = Paginator(products, 50)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'page_obj': page_obj}
        return render(request, 'storage/products.html', context)