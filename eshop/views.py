from django.shortcuts import render


from django.views.generic import ListView,DetailView, CreateView
from django.db.models import F
from .models import Product

def index(request):
    return render(request, 'index.html', {})


def category_detail(request, id):
    return render(request, 'index.html', {})


class ProductDetail(DetailView):
    model = Product
    template_name = ''
    context_object_name = 'product'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['name'] = 'Product'
        context.update({
            'product':Product.objects.all(),
            'Views':Product.objects.filter(pk=Product.pk).update(views=F('views') + 1)
        })


def cart_detail(request):
    return render(request, 'index.html', {})


def order_detail(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'index.html', {})


def add_to_cart(request, id):
    return render(request, 'index.html', {})